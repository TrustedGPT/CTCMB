import json

from make_answer.chat.chat_invoker import ChatInvoker


def spd(data: dict, llm: ChatInvoker) -> dict:
    prompt = (f"你是一个中医专家，请根据患者的症状，参考症候定义，判断当前患者属于每一个症候对应的概率，概率取值范图在0%~100%内，0%为无可能，100%一定是，\n患者症状:{data['descript']},症候定义:{data['symptoms']}\n"
                '返回格式：1.以json格式的list返回，一个可能的示例：[{"zheng_hou_name":" ","gai_lv": " ", "description":" "},{"zheng_hou_name":" ","gai_lv": " ", "description":" "}]}'
              f"2.按照概率从大到小（递减）的顺序，3.你必须返回参考症候定义的所有病症，同时不得涉及参考症候外的症候。")
    response = llm.chat(prompt)
    data["answer"] = response
    return data


