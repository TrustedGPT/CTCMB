from evaluate.works.scoring import calculate_micro_f1
from loguru import logger
import json
from evaluate.works.scoring import rouge1L_scoring, bert_scoring, BLEU

def CmeEE(standard_data: dict, llm_data: dict) -> dict:
    # try:
    #     micro_F1 = calculate_micro_f1(standard_data["entities"], llm_data["answer"])
    # except Exception:
    #     raw_data = {"standard_data": standard_data, "llm_data": llm_data}
    #     logger.exception(f"Calculation fails, consider returning 0 directly. Raw data: {raw_data}")
    #     micro_F1 = 0.0
    #
    # return micro_F1
    answer = json.dumps(standard_data['entities'], ensure_ascii=False, indent=4)
    response = llm_data["answer"]

    rouge_1, rouge_l = rouge1L_scoring(response, answer)
    bert = bert_scoring(response, answer)
    bleu = BLEU(response, answer)

    return {"rouge_1": rouge_1, "rouge_l": rouge_l, "bert": bert, "bleu": bleu}
