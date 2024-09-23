import os
import re

from loguru import logger

from chat.LlmChat import LlmChat
from score_func.scoring import multiple_choice_score


def tcm_ds(data: dict, llm: LlmChat,model:str) -> float:
    prompt = (f"接下来有一道多选题，请给出正确选项，不需要回答任何错误选项的信息，答案以一个列表形式返回"
              f"{data['question']}，选项{data['options']}")

    response = llm.chat(prompt)
    logger.info(response)
    max_option = chr(len(data["options"]) + 64)
    extract_option = re.compile(rf"[A-{max_option}]")
    # 遍历匹配结果，如果结果不是从小到大，则保留第一个到字母顺序递增的结果
    response_option = []
    for matcher in extract_option.findall(response):
        if not response_option or ord(matcher) > ord(response_option[-1]):
            response_option.append(matcher)
    score=multiple_choice_score(response_option, data["answer"])
    log_message = f"[{os.getpid()}] prompt: {prompt}\nresponse: {response_option}, \nanswer: {data['answer']}\n"
    # 记录日志
    logger.info(log_message)
    return score
