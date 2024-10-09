import json


def SCD_scoring(standard_data: dict, llm_data: dict) -> dict:
    response = llm_data["answer"]
    answer = {k: v for k, v in standard_data.items() if k == "optimized_past_medical_history" or k == "optimized_present_illness"}
    answer_pro = json.dumps(answer, ensure_ascii=False, indent=4)

    #rouge_1, rouge_l = rouge1L_scoring(response, answer_pro)
    #bert = bert_scoring(response, answer_pro)
    #bleu=BLEU(response,answer_pro)
    return 0
