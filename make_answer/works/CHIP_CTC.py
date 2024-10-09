import re

from make_answer.chat.chat_invoker import ChatInvoker


def CHIP_CTC(data: dict, llm: ChatInvoker) -> dict:
    prompt=(f"类别名称列表如下：\n"
            f"[Diagnostic、Enrollment in other studies、Researcher Decision、Data Accessible、Ethnicity、Therapy or Surgery、Encounter、Healthy、Sexual related、Non-Neoplasm Disease Stage、Device、Education、Allergy Intolerance、Literacy、Laboratory Examinations、Oral related、Alcohol Consumer、Special Patient Characteristic、Ethical Audit、Receptor Status、Addictive Behavior、Disease、Smoking Status、Disabilities、Nursing、Organ or Tissue Status、Bedtime、Life Expectancy、Risk Assessment、Symptom、Capacity、Compliance with Protocol、Address、Neoplasm Status、Diet、Multiple、Pregnancy-related Activity、Blood Donation、Exercise、Sign、Pharmaceutical Substance or Drug、Age、Gender、Consent]\n"
            f"请将下面的医学文本进行分类，请根据类别名称列表输出具体的类别名称。{data['text']}。只回答类别名称，不需要其余解释。你不需要阐述不是某个类别，只需要说明是哪个类别"
    )
    response = llm.chat(prompt)
    pattern = re.compile(r"\b[a-zA-Z]+(?: [a-zA-Z]+)*\b")
    response = pattern.findall(response)
    choice = ""
    if len(response):
        choice = response[-1]
    data["answer"] = choice

    return data
