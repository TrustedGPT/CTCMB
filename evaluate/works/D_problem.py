def single_d(standard_data: dict, llm_data: dict) -> float:
    score = 0
    for index, question in enumerate(standard_data["question"]):
        choice = llm_data["question"][index]["answer"]
        answer = question["answer"][0]
        if choice != "" and choice.lower() == answer.lower():
            score += 1

    return score / len(standard_data["question"])
