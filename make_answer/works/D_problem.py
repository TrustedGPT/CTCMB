import re

from make_answer.chat.chat_invoker import ChatInvoker


def single_d(data: dict, llm: ChatInvoker) -> dict:
    max_option = "D"
    while max_option in data["share_content"]:
        max_option = chr(ord(max_option) + 1)
    else:
        max_option = chr(ord(max_option) - 1)
    extract_choice = re.compile(rf".*?([A-{max_option}]).*", re.DOTALL)
    prompt_answer_list = []
    for question in data["question"]:
        prompt = f'接下来是一道共用选项的题目，题干如下：{data["share_content"]}\n，请根据题干内容，为以下题目进行答题。\n'
        prompt += "这道题是单选题，你只需要给给出选项字母序号，不能给出其他内容。\n"
        prompt += question["sub_question"].replace("\n", " ")
        response = llm.chat(prompt)
        match = extract_choice.match(response)
        choice = ""
        if match:
            choice = match.group(1)
        question["answer"] = choice
        prompt_answer_list.append(
            {"prompt": prompt, "response": response, "match": match}
        )

    return data
