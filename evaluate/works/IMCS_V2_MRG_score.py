import json

from evaluate.works.scoring import rouge1L_scoring, bert_scoring, BLEU


def IMCS_V2_MRG(standard_data: dict, llm_data: dict) -> dict:
    answer_0 = json.dumps(standard_data['report'][0], ensure_ascii=False, indent=4)
    answer_1 = json.dumps(standard_data['report'][1], ensure_ascii=False, indent=4)
    response = llm_data["answer"]

    rouge_1_0, rouge_l_0 = rouge1L_scoring(response, answer_0)
    bert_0 = bert_scoring(response, answer_0)
    bleu_0=BLEU(response,answer_0)
    rouge_1_1, rouge_l_1 = rouge1L_scoring(response, answer_1)
    bert_1 = bert_scoring(response, answer_1)
    bleu_1 = BLEU(response, answer_1)
    rouge_1=max(rouge_1_0,rouge_1_1)
    rouge_l=max(rouge_l_0,rouge_l_1)
    bert=max(bert_0,bert_1)
    bleu=max(bleu_0,bleu_1)

    return {"rouge_1": rouge_1, "rouge_l": rouge_l, "bert": bert,"bleu":bleu}
