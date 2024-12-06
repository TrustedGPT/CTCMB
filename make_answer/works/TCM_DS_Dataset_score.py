import re

from make_answer.chat.chat_invoker import ChatInvoker


def tcm_ds(data: dict, llm: ChatInvoker) -> dict:
    prompt = (f"接下来有一道多选题，请给出正确选项，不需要回答任何错误选项的信息，答案以一个列表形式返回"
              f"{data['question']}，选项{data['options']}")

    response = llm.chat(prompt)
    max_option = chr(len(data["options"]) + 64)
    extract_option = re.compile(rf"[A-{max_option}]")
    # 遍历匹配结果，如果结果不是从小到大，则保留第一个到字母顺序递增的结果
    response_option = []
    for matcher in extract_option.findall(response):
        if not response_option or ord(matcher) > ord(response_option[-1]):
            response_option.append(matcher)
    data["answer"] = "".join(response_option)

    return data
