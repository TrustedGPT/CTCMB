from make_answer.chat.chat_invoker import ChatInvoker


def IMCS_V2_MRG(data: dict, llm: ChatInvoker) -> dict:
    prompt = (
        f"信息抽取的表单为：'主诉'：\n'现病史'：\n'辅助检查'：\n'既往史'：\n'诊断'：\n'建议'：\n 表单需要严格满足json格式。要求：1.对于每个表项，从对话中提取并总结对应的信息进行填充；2.同一类别的多种信息用句号'。'分隔；3.如果表项的内容在对话中没有提及，将表项的值置为“无”；4.输出格式与信息抽取的表单一致，不要输出其它格式。\n"
        f"从以下医患对话中提取信息，填充以上表单：{data['question']}")
    response = llm.chat(prompt)
    data["answer"] = response

    return data
