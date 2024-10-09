from evaluate.works.scoring import rouge1L_scoring, bert_scoring,BLEU


def tcm_clin(standard_data: dict, llm_data: dict) -> dict:
    response = llm_data["answer"]
    answer = f"{standard_data['syndrome']}。{standard_data['lcd_name']}。"

    rouge1, rougel = rouge1L_scoring(response, answer)
    bert = bert_scoring(response, answer)
    bleu=BLEU(response,answer)

    return {"rouge_1": rouge1, "rouge_l": rougel, "bert": bert,"bleu":bleu}
