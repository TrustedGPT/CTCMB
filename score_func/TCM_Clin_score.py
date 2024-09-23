import time
import os
from loguru import logger
import json
import openai

from chat.LlmChat import LlmChat
from score_func.scoring import rouge1L_scoring, bert_scoring,BLEU


def tcm_clin(data: dict, llm: LlmChat,model:str) -> dict:
    prompt = (
        f'某病人的主诉为{data["chief_complaint"]}，其病情描述为{data["description"]}，其体格检查结果为{data["detection"]}，'
        f'请判断这位病人的病症的标准化的中医辨证结果为？西医或者国际通用的的疾病名称是？'
        f'你只需要回答疾病名称，不需要作其他任何解释。回答格式为——“中医辨证结果。西医疾病名称”')
    while True:
        try:
            response = llm.chat(prompt)
            break
        except openai.RateLimitError as e:
            time.sleep(10)
            continue
    answer = f"{data['syndrome']}。{data['lcd_name']}。"
    log_message = f"[{os.getpid()}] prompt: {prompt}\nresponse: {response}, \nanswer: {answer}\n"
    # 记录日志
    logger.info(log_message)
    rouge1, rougel = rouge1L_scoring(response, answer)
    bert = bert_scoring(response, answer)
    bleu=BLEU(response,answer)
    return {"rouge_1": rouge1, "rouge_l": rougel, "bert": bert,"bleu":bleu}
