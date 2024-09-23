import os
import time
import re
import openai
import json
from loguru import logger
from chat.LlmChat import LlmChat


def single_d(data: dict, llm: LlmChat,model:str) -> float:
    max_option = "D"
    while max_option in data["share_content"]:
        max_option = chr(ord(max_option) + 1)
    else:
        max_option = chr(ord(max_option) - 1)
    extract_choice = re.compile(rf".*?([A-{max_option}]).*", re.DOTALL)
    prompt_answer_list = []
    score = 0
    for question in data["question"]:
        prompt = f'接下来是一道共用选项的题目，题干如下：{data["share_content"]}\n，请根据题干内容，为以下题目进行答题。\n'
        prompt += "这道题是单选题，你只需要给给出选项字母序号，不能给出其他内容。\n"
        prompt += question["sub_question"].replace("\n", " ")
        answer = question["answer"][0]
        response = llm.chat(prompt)
        match = extract_choice.match(response)
        choice = ""
        if match:
            choice = match.group(1)
        if choice != "" and match.group(1).lower() == answer.lower():
            score += 1
        prompt_answer_list.append(
            {"prompt": prompt, "response": response,  "answer": answer, "match": match}
        )

    # 记录日志
    logger.info(prompt_answer_list)

    return score / len(data["question"])
