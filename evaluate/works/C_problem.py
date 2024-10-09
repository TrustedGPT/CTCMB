def single_c(standard_data: dict, llm_data: dict) -> float:
    score = 0
    for index, question in enumerate(standard_data["question"]):
        answer = question["answer"][0]
        choice = llm_data["question"][index]["answer"]
        if choice != "" and choice.lower() == answer.lower():
            score += 1

    return score / len(standard_data["question"])
