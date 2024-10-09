from make_answer.chat.chat_invoker import ChatInvoker


def tcmeee(data: dict, llm: ChatInvoker) -> dict:
    prompt = f"{data['question']}"
    response = llm.chat(prompt)
    data["answer"] = response

    return data
