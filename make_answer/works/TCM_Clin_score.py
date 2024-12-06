from make_answer.chat.chat_invoker import ChatInvoker


def tcm_clin(data: dict, llm: ChatInvoker) -> dict:
    prompt = (
        f'某病人的主诉为{data["chief_complaint"]}，其病情描述为{data["description"]}，其体格检查结果为{data["detection"]}，'
        f'请判断这位病人的病症的标准化的中医辨证结果为？西医或者国际通用的的疾病名称是？'
        f'你只需要回答疾病名称，不需要作其他任何解释。回答格式为——“中医辨证结果。西医疾病名称”')
    response = llm.chat(prompt)
    data["answer"] = response

    return data
