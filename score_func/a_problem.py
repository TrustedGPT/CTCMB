import os
import re
import json

from loguru import logger
from chat.LlmChat import LlmChat


def single_a(data: dict, llm: LlmChat,model:str) -> int:
    prompt = f"以下是一道单选题，你需要给出选项字母序号，你不需要给出其他解释。{data['title']}?{str(data['options'])}"
    response = llm.chat(prompt)
    # 判断选项从A-len(options)的字母
    max_option = chr(len(data["options"]) + 64)
    extract_choice = re.compile(rf".*?([A-{max_option}]).*", re.DOTALL)
    # 从response中找到第一个选项
    match = extract_choice.match(response)
    score = 0
    choice = ""
    if match:
        choice = match.group(1)
    if choice != "" and choice.lower() == data["answer"].lower():
        score = 1
    log_message = f"[{os.getpid()}] prompt: {prompt}\nresponse: {response}, \nanswer: {data['answer']}\n"
    # 记录日志
    logger.info(log_message)
    return score
