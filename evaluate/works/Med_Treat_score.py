import json

from evaluate.works.scoring import rouge1L_scoring, bert_scoring, BLEU


def med_treat(standard_data: dict, llm_data: dict) -> dict:
    answer = {
        "方剂名称": standard_data["answer"]["Name of the formula"], "方剂组成": standard_data["answer"]["Composition of the formula"],
        "方剂用法": standard_data["answer"]["Usage"]
    }
    answer = json.dumps(answer, ensure_ascii=False, indent=4)
    response = llm_data["answer"]

    rouge_1, rouge_l = rouge1L_scoring(response, answer)
    bert = bert_scoring(response, answer)
    bleu=BLEU(response,answer)
    return {"rouge_1": rouge_1, "rouge_l": rouge_l, "bert": bert,"bleu":bleu}
