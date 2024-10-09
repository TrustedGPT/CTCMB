import re

from make_answer.chat.chat_invoker import ChatInvoker


def tcm_did(data: dict, llm: ChatInvoker) -> dict:
    prompt = (f'接下来是一道改错题，判断对错，并给出解释。'
              f'必须先说明“对”或者“错”，然后再说明原因。\n'
              f'{data["question"]}')

    response = llm.chat(prompt)
    correct_or_error = re.compile(r"([对错])", re.DOTALL)
    matcher = correct_or_error.findall(response)
    choice = ""
    if matcher:
        choice = matcher[0]
    response = {
        "answer": choice,
        "explanation": response
    }
    data["answer"] = response

    return data
