def tcm_srt(standard_data: dict, llm_data: dict) -> float:
    choice = llm_data["answer"]
    score = 0
    if choice != "" and choice.lower() == standard_data["answer"].lower():
        score = 1

    return score
