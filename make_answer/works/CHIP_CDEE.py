import json
import re
from typing import final

from make_answer.chat.chat_invoker import ChatInvoker


def is_valid_json_list(response):
    try:
        # 尝试将响应解析为 JSON
        json_data = json.loads(response)
        # 检查是否为列表，并且每个对象都包含必需的字段
        if isinstance(json_data, list):
            required_keys = {"core_name", "tendency", "character","anatomy_list"}
            for item in json_data:
                if not all(key in item for key in required_keys):
                    return False
            return True
        return False
    except json.JSONDecodeError:
        return False


def clean_and_format_response(response):
    # 去除多余空白符号
    cleaned_response = re.sub(r'\s+', ' ', response.strip())
    
    # 替换分散的对象结构为标准的 JSON 列表结构
    cleaned_response = cleaned_response.replace("}, {", "},{")
    cleaned_response = "[" + cleaned_response + "]"
    
    try:
        # 尝试将其转换为 JSON
        json_data = json.loads(cleaned_response)
        print(json_data)
        return json_data
    except json.JSONDecodeError:
        print("Invalid JSON format after formatting.")
        return []


# 主函数处理逻辑
def process_response(response):
    # 首先检查是否符合要求的 JSON 列表格式
    if is_valid_json_list(response):
        print("Response is already in valid JSON format.")
        return json.loads(response)
    else:
        # 如果不符合要求，进行清理和格式化
        print("Response is not in valid format. Proceeding with cleanup and formatting.")
        return clean_and_format_response(response)


def CHIP_CDEE(data: dict, llm: ChatInvoker) -> dict:
    prompt = (
        f"从下面的病历或者医学影像报告中抽取所有的临床发生事件,直接抽取临床发现事件的四个属性:core_name(指疾病名称或者由疾病引发的症状，也包括患一般情况如饮食等。)、tendency(“不确定”或“否定”，肯定的情况不标注发生状态)、character(对主体词的发生时序特征、轻重程度、形态颜色等多个维度的刻画，也包括疾病的起病缓急、突发)、anatomy_list(指主体词发生在患者的身体部位，也包括组织,也包括部位的方向和数量)\n"
        f"输出格式为:\n“core_name”: 主体词\n“tendency”: 发生状态,如果没有发生状态，默认为""\n“character”: 描述词，列表结构，如果没有描述词，默认为[]\n“anatomy_list”: 解剖部位，列表结构，如果没有解剖部位，默认为[]\n"
        f"表单需要严格满足json格式，符合python中列表的格式，不需要多余的解释。请从以下病历或者医学影像所见报告中抽取临床发现事件：{data['text']}")
    response = llm.chat(prompt)
    try:
        response_new = response.strip().split('```json')[1].strip()
        response_end = response_new.strip("```").strip()
    except:
        response_end = response.strip("```").strip()
    res=process_response(response_end)
    data["answer"] = res

    return data
