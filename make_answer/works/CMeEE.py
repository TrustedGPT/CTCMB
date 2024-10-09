import json
import re

from make_answer.chat.chat_invoker import ChatInvoker


def is_valid_json_list(response):
    try:
        # 尝试将响应解析为 JSON
        json_data = json.loads(response)
        # 检查是否为列表，并且每个对象都包含必需的字段
        if isinstance(json_data, list):
            required_keys = {"type", "entity"}
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


def CmeEE(data: dict, llm: ChatInvoker) -> dict:
    prompt=f"从下面的医学文本中提取出所有的医学实体，并根据实体的类型进行分类。注意表单需要严格满足json格式，符合python中列表的格式。实体类别包括 “dru”(表示药物),“equ”（表示设备）,“dep”（表示医院科室）,“mic”（表示微生物类）,“bod”（表示身体部位）,“pro”（表示医疗操作）,“ite”（表示医学检验项目）,“sym”（表示症状）,“dis”（表示疾病）,\n。输出格式为：\n“type”: 实体类别\n”entity“: 实体名称\n 请对以下医学文本进行实体识别: {data['text']}"
    response = llm.chat(prompt)
    response_end = ""
    try:
        response_new = response.strip().split('```json')[1].strip()
        response_end = response_new.strip("```").strip()
    except:
        response_end = response.strip("```").strip()
    finally:
        data["answer"] = response_end
    return data
