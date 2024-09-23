import os

from loguru import logger

from chat.LlmChat import LlmChat
from score_func.scoring import rouge1L_scoring, bert_scoring, BLEU


def tcm_litdata(data: dict, llm: LlmChat,model:str) -> dict:
    #llm = LlmChat(llm.model)
    
    rouge1_avg = 0
    rougel_avg = 0
    bert_avg = 0
    bleu_avg=0
    prompt_response_list = []
    for question in data["annotations"]:
        prompt = f'这是一段经典文献，其内容是{data["text"]}。\n'
        prompt += f'你只能摘取文献中的原文进行回答，每个回答只有1到2句话。{question["Q"]}'
        response = llm.chat(prompt)
        rouge1, rougel = rouge1L_scoring(response, question["A"])
        bert = bert_scoring(response, question["A"])
        bleu=BLEU(response,question["A"])
        rouge1_avg += rouge1
        rougel_avg += rougel
        bert_avg += bert
        bleu_avg+=bleu
        prompt_response_list.append(
            {"prompt": prompt, "response": response, "answer": question["A"], "rouge1": rouge1, "rougel": rougel, "bert": bert,"bleu":bleu}
        )
        #prompt = ""
    rouge1_avg /= len(data["annotations"])
    rougel_avg /= len(data["annotations"])
    bert_avg /= len(data["annotations"])
    bleu_avg /= len(data["annotations"])
    log_message=f"[{os.getpid()}] prompt_response_list: {prompt_response_list}, rouge1_avg: {rouge1_avg}, rougel_avg: {rougel_avg}, bert_avg: {bert_avg}"
    # 记录日志
    logger.info(log_message)
    return {"rouge_1": rouge1_avg, "rouge_l": rougel_avg, "bert": bert_avg,"bleu":bleu_avg}
