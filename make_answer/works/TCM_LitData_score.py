from make_answer.chat.chat_invoker import ChatInvoker


def tcm_litdata(data: dict, llm: ChatInvoker) -> dict:
    for question in data["annotations"]:
        prompt = (f'这是一段经典文献，其内容是{data["text"]}。\n'
                f'你只能摘取文献中的原文进行回答，每个回答只有1到2句话。{question["Q"]}')
        response = llm.chat(prompt)
        question["answer"] = response

    return data
