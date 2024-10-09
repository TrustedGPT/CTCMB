from evaluate.works.scoring import rouge1L_scoring, bert_scoring,BLEU


def tcm_ft(standard_data: dict, llm_data: dict) -> dict:
    response = llm_data["answer"]

    rouge_1, rouge_l = rouge1L_scoring(response, standard_data["answer"])
    bert = bert_scoring(response, standard_data["answer"])
    bleu=BLEU(response, standard_data["answer"])

    return {"rouge_1": rouge_1, "rouge_l": rouge_l, "bert": bert,"bleu":bleu}
