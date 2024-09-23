import os
import re
import json
from loguru import logger
from chat.LlmChat import LlmChat


def single_c(data: dict, llm: LlmChat,model:str) -> float:
    score = 0
    prompt_answer_list = []
    for question in data["question"]:
        prompt = f'共用题干的题目如下：{data["share_content"]}\n请根据题干内容进行答题。\n'
        prompt_answer_list = []
        prompt += "每道题是单选题，只需要给出选项字母序号。\n"
        prompt += question["sub_question"].replace("\n", " ")
        answer = question["answer"][0]
        response = llm.chat(prompt)
        max_option = "D"
        while max_option in question["sub_question"]:
            max_option = chr(ord(max_option) + 1)
        else:
            max_option = chr(ord(max_option) - 1)
        extract_choice = re.compile(rf".*?([A-{max_option}]).*", re.DOTALL)
        # 从response中找到第一个选项
        match = extract_choice.match(response)
        choice = ""
        if match:
            choice = match.group(1)
        if choice != "" and choice.lower() == answer.lower():
            score += 1
        prompt_answer_list.append(
            {"prompt": prompt,
             "response": response,
             "answer": answer,
             "match": match}
        )

    # 记录日志
    logger.info(prompt_answer_list)
    return score / len(data["question"])
