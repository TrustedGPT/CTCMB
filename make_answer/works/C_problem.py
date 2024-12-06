import re

from make_answer.chat.chat_invoker import ChatInvoker


def single_c(data: dict, llm: ChatInvoker) -> dict:
    prompt_answer_list = []
    for question in data["question"]:
        prompt = f'共用题干的题目如下：{data["share_content"]}\n请根据题干内容进行答题。\n'
        prompt += "每道题是单选题，只需要给出选项字母序号。\n"
        prompt += question["sub_question"].replace("\n", " ")
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
        question["answer"] = choice
        prompt_answer_list.append(
            {"prompt": prompt, "response": response, "match": match}
        )

    return data