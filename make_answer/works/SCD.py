from make_answer.chat.chat_invoker import ChatInvoker


def SCD(data: dict, llm: ChatInvoker) -> dict:
    prompt = (f"你是一个经验丰富的中西医全科专家,你已根据问诊对话写出了病例，包括现病史、既往史信息，现在需要你根据补充问诊对话内容对原病例内容作出调整，然后按指定格式输出。"
              f"[现病史：现病史指患者本次疾病的发生、演变、诊疗等方面的详细情况。\n记录内容及顺序：\n1.发病时间及发病原因；如患者于xxx前因xxx导致xxx；若没提到病因时写无明显诱因；2.主要症状及发展情况：包括发生顺序，部位，性质，持续时间，程度，缓解或加剧因素及演变情况；3.伴随症状：伴随主症同时存在的症状，医生问有无谋症状，患者回答有的症状；4.阴性症状：医生问有无谋症状，患者回答无的症状,不能出现病名；5.发病以来诊治或用药过程及效果；6.其他本次需治疗疾病情况；7.情志、食量、睡眠、大小便状况；例如：大小便次数、是否成形、颜色等状况；]\n"
              f"[既往史：患者过去的健康和疾病情况，与主诉无直接关系。\n包括1.既往疾病史：疾病名称、患病时间、治疗情况2.传染病史：疾病名称、患病时间、治疗情况3.手术史：手术原因、手术日期、手术名称、手术结果4.食物或药物过敏史：过敏物质5.预防接种史：疫苗名称、接种时间6.家族史：与患者类似疾病、遗传疾病7.不良习惯：有无抽烟喝酒等不良习惯,若没有写无]\n"
              f"根据补充对话内容及要求，客观调优已写病例结果，不输出（）及其中的内容，行尾不写标点，且不要写多余描述。输出格式为：\n"
              f"'调优现病史':（要求：忽略未提及的要素！200字以内）\n'调优既往史'：\n问诊对话为：{data['main_conversation']},既往史为：{data['past_medical_history']},现病史为：{data['present_illness']}，补充对话为：{data['sub_conversation']}")
    response = llm.chat(prompt)

    try:
        response_new = response.strip().split('```json')[1].strip()
        response_end = response_new.strip("```").strip()
    except:
        response_end = response.strip("```").strip()
    data["answer"] = response_end

    return data
