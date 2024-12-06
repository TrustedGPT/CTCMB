from make_answer.chat.chat_invoker import ChatInvoker


def med_treat(data: dict, llm: ChatInvoker) -> dict:
    prompt = (f'{data["question"]}，返回的格式为一个json格式：{{"方剂名称": , "方剂组成": , "方剂用法": }}，'
              f'你不能返回除这个格式之外的任何内容。')
    response = llm.chat(prompt)
    data["answer"] = response

    return data
