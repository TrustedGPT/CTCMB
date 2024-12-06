import re

from make_answer.chat.chat_invoker import ChatInvoker


def single_b(data: dict, llm: ChatInvoker) -> dict:
    prompt = f"以下是一到单选题，你需要给给出选项字母序号，你不需要给出其他解释。{data['title']}?{str(data['options'])}"
    response = llm.chat(prompt)
    # 判断选项从A-len(options)的字母
    max_option = chr(len(data["options"]) + 64)
    extract_choice = re.compile(rf".*?([A-{max_option}]).*", re.DOTALL)
    # 从response中找到第一个选项
    match = extract_choice.match(response)
    choice = ""
    if match:
        choice = match.group(1)
    data["answer"] = choice

    return data
