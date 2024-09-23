import os
import re
import json
from loguru import logger

from chat.LlmChat import LlmChat
from score_func.scoring import judgement_correction_score


def tcm_did(data: dict, llm: LlmChat,model:str) -> float:
    prompt = (f'接下来是一道改错题，判断对错，并给出解释。'
              f'必须先说明“对”或者“错”，然后再说明原因。\n'
              f'{data["question"]}')

    response = llm.chat(prompt)
    logger.info(response)
    correct_or_error = re.compile(r"([对错])", re.DOTALL)
    matcher = correct_or_error.findall(response)
    response = {
        "answer": matcher[0],
        "explanation": response
    }
    try:
        score = judgement_correction_score(response, data)
    except Exception as e:
        logger.error(f"[{os.getpid()} caculate score error] {e} [data: {data}][response: {response}]")
        score = 0

    log_message = f"[{os.getpid()}] prompt: {prompt}\nresponse: {response}, \nanswer: {data['answer']}\n,explanation:{data['explanation']}"
    # 记录日志
    logger.info(log_message)
    return score
