import re

from make_answer.chat.chat_invoker import ChatInvoker


def tcm_srt(data: dict, llm: ChatInvoker) -> dict:
    prompt = (f"接下来是一道逻辑推理题，前提：{data['premise']}，论述：{data['hypothesis']}，"
              f"目前有两个选项：{str(data['options'])}, 请给出你的答案对应的序号，只能给出答案对应的序号，不能输出其他的任何内容。")
    response = llm.chat(prompt)
    extract_option = re.compile(r".*([AB]).*", re.DOTALL)
    match = extract_option.match(response)
    choice = ""
    if match:
        choice = match.group(1)
    data["answer"] = choice
    return data
