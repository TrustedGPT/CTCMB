import json

from evaluate.works.scoring import rouge1L_scoring, bert_scoring, BLEU


def tcm_chgd(standard_data: dict, llm_data: dict) -> dict:
    answer = json.dumps(standard_data['answer'], ensure_ascii=False, indent=4)
    response = llm_data["answer"]

    rouge_1, rouge_l = rouge1L_scoring(response, answer)
    bert = bert_scoring(response, answer)
    bleu=BLEU(response,answer)

    return {"rouge_1": rouge_1, "rouge_l": rouge_l, "bert": bert,"bleu":bleu}
