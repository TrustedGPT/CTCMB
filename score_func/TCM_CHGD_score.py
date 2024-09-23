import time
import json
import openai
import os
from loguru import logger
from chat.LlmChat import LlmChat
from score_func.scoring import rouge1L_scoring, bert_scoring,BLEU


def tcm_chgd(data: dict, llm: LlmChat,model:str) -> dict:
    prompt = f"{data['question']}"
    while True:
        try:
            response = llm.chat(prompt)
            break
        except openai.RateLimitError:
            time.sleep(10)
            continue

    answer = json.dumps(data['answer'], ensure_ascii=False, indent=4)
    log_message = f"[{os.getpid()}] prompt: {prompt}\nresponse: {response}, \nanswer: {answer}\n"
    # 记录日志
    logger.info(log_message)
    rouge_1, rouge_l = rouge1L_scoring(response, answer)
    bert = bert_scoring(response, answer)
    bleu=BLEU(response,answer)
    return {"rouge_1": rouge_1, "rouge_l": rouge_l, "bert": bert,"bleu":bleu}
