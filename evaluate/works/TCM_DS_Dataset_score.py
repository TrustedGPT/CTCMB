from evaluate.works.scoring import multiple_choice_score


def tcm_ds(standard_data: dict, llm_data: dict) -> float:
    response = llm_data["answer"]

    score=multiple_choice_score(response, standard_data["answer"])

    return score
