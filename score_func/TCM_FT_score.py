import time
import os
import openai
import json
from loguru import logger
from chat.LlmChat import LlmChat
from score_func.scoring import rouge1L_scoring, bert_scoring,BLEU


def tcm_ft(data: dict, llm: LlmChat,model:str) -> dict:
    prompt = f"用一段话回答这个问题，不能使用分点论述，需要尽可能的总结。{data['question']}"
    while True:
        try:
            response = llm.chat(prompt)
            break
        except openai.RateLimitError:
            logger.exception(f"[{os.getpid()}] rate limit error!")
            time.sleep(10)
            continue
    log_message = f"[{os.getpid()}] prompt: {prompt}\nresponse: {response}, \nanswer: {data['answer']}\n"
    # 记录日志
    logger.info(log_message)
    rouge_1, rouge_l = rouge1L_scoring(response, data["answer"])
    bert = bert_scoring(response, data["answer"])
    bleu=BLEU(response,data["answer"])
    return {"rouge_1": rouge_1, "rouge_l": rouge_l, "bert": bert,"bleu":bleu}
