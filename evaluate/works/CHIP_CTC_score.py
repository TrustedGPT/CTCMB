def CHIP_CTC(standard_data: dict, llm_data: dict) -> float:
    score_s = 0
    if llm_data["answer"]==standard_data['label']:
        score_s=1

    return score_s



