import json
import time
import os
import openai
from loguru import logger
from chat.LlmChat import LlmChat
from score_func.scoring import rouge1L_scoring, bert_scoring,BLEU


def med_treat(data: dict, llm: LlmChat,model:str) -> dict:
    prompt = (f'{data["question"]}，返回的格式为一个json格式：{{"方剂名称": , "方剂组成": , "方剂用法": }}，'
              f'你不能返回除这个格式之外的任何内容。')
    while True:
        try:
            response = llm.chat(prompt)
            break
        except openai.RateLimitError:
            time.sleep(10)
            continue
    answer = {
        "方剂名称": data["answer"]["Name of the formula"], "方剂组成": data["answer"]["Composition of the formula"],
        "方剂用法": data["answer"]["Usage"]
    }
    answer = json.dumps(answer, ensure_ascii=False, indent=4)
    log_message = f"[{os.getpid()}] prompt: {prompt}\nresponse: {response}, \nanswer: {answer}\n"
    # 记录日志
    logger.info(log_message)
    rouge_1, rouge_l = rouge1L_scoring(response, answer)
    bert = bert_scoring(response, answer)
    bleu=BLEU(response,answer)
    return {"rouge_1": rouge_1, "rouge_l": rouge_l, "bert": bert,"bleu":bleu}
