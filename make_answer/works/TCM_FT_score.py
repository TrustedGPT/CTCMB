from make_answer.chat.chat_invoker import ChatInvoker


def tcm_ft(data: dict, llm: ChatInvoker) -> dict:
    prompt = f"用一段话回答这个问题，不能使用分点论述，需要尽可能的总结。{data['question']}"
    response = llm.chat(prompt)
    data["answer"] = response

    return data
