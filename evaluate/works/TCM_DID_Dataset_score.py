import os
import json

from loguru import logger
from evaluate.works.scoring import judgement_correction_score


def tcm_did(standard_data: dict, llm_dict: dict) -> float:
    response = llm_dict["answer"]
    if isinstance(response, str):
        try:
            response = json.loads(response)
        except json.decoder.JSONDecodeError:
            logger.exception("")
    try:
        score = judgement_correction_score(response, standard_data)
    except Exception as e:
        logger.error(f"[{os.getpid()} caculate score error] {e} [data: {standard_data}][response: {response}]")
        score = 0

    return score
