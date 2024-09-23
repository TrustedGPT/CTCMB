import os
import time
import json
import openai
from loguru import logger

from chat.LlmChat import LlmChat
from score_func.scoring import rouge1L_scoring, bert_scoring, BLEU


def tcmeee(data: dict, llm: LlmChat,model:str) -> dict:
    prompt = f"{data['question']}"
    while True:
        try:
            response = llm.chat(prompt)
            break
        except openai.RateLimitError as e:
            time.sleep(0.5)
            continue
    log_message = f"[{os.getpid()}] prompt: {prompt}\nresponse: {response}, \nanswer: {data['answer']}\n"
    # 记录日志
    logger.info(log_message)
    rouge_1, rouge_l = rouge1L_scoring(json.dumps(response,ensure_ascii=False,indent=4), json.dumps(data["answer"], ensure_ascii=False,indent=4))
    bert = bert_scoring(json.dumps(response,ensure_ascii=False,indent=4), json.dumps(data["answer"],ensure_ascii=False,indent=4))
    bleu=BLEU(json.dumps(response,ensure_ascii=False,indent=4),json.dumps(data["answer"],ensure_ascii=False,indent=4))
    return {"rouge_1": rouge_1, "rouge_l": rouge_l, "bert": bert,"bleu":bleu}
