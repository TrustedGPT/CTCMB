import os
import time
import json
import openai
from loguru import logger
from sympy import print_glsl

from chat.LlmChat import LlmChat
from score_func.scoring import rouge1L_scoring,BLEU,bert_scoring


def spd_score(data: dict, llm: LlmChat, model:str) -> dict:
    prompt = (f"你是一个中西医全科专家，请景据患者的症状，参考症候定义，判断当前惠者属于每一个症候对应的概率，概率取值范图在0%~100%内，0%为无可能，100%一定是，以json返回\n患者症状:{data['descript']},症候定义:{data['symptoms']}\n"
                f"返回格式，概率高的排数组前面,需要严格满足json格式\n:'zheng_hou_name':'症候名'，\n'gai_lv':'概率',\n'description':'概率说明'")
    while True:
        try:
            response = llm.chat(prompt)
            break
        except openai.RateLimitError as e:
            time.sleep(0.5)
            continue
    answer_set = {}
    index = 0
    data['responses'] = json.loads(data['responses'])
    k = len(data['responses']) / 2
    for i in data['responses']:
        if index < k:
            answer_set[i['zheng_hou_name']] = i['description']
            index =  index + 1
    log_message = f"[{os.getpid()}] question: {data['descript']}\n{data['responses']}responses: {response}, \nanswer: {data['responses']}\n"
    # 记录日志
    logger.info(log_message)
    print(response)
    res = json.loads(response)
    score = 0
    j = 0
    for i in res:
        if j > k:
            break
        if i['zheng_hou_name' ]  in answer_set:
            score += 0.5
            score = score + bert_scoring(answer_set[i['zheng_hou_name']], i['description'])/2
        j += 1
    return score/k


