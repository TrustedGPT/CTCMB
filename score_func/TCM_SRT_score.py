import os
import re

from loguru import logger
from chat.LlmChat import LlmChat


def tcm_srt(data: dict, llm: LlmChat,model:str) -> float:
    prompt = (f"接下来是一道逻辑推理题，前提：{data['premise']}，论述：{data['hypothesis']}，"
              f"目前有两个选项：{str(data['options'])}, 请给出你的答案对应的序号，只能给出答案对应的序号，不能输出其他的任何内容。")
    response = llm.chat(prompt)
    extract_option = re.compile(r".*([AB]).*", re.DOTALL)
    match = extract_option.match(response)
    choice = ""
    if match:
        choice = match.group(1)
    log_message=f"[{os.getpid()}] prompt: {prompt}\nresponse: {response}\nanswer: {data['answer']}"
    score = 0
    if choice != "" and choice.lower() == data["answer"].lower():
        score = 1
    # 记录日志
    logger.info(log_message)
    return score
