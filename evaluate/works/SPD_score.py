import json

from loguru import logger

from evaluate.works.scoring import bert_scoring


def spd_score(standard_data: dict, llm_data: dict) -> float:
    answer_set = {}
    index = 0
    standard_data['responses'] = json.loads(standard_data['responses'].replace('```json\n','').replace('\n```','').replace('```\n',''))
    k = max(1, round(len(standard_data['responses']) / 2))
    logger.info(f"k={k}")
    for i in standard_data['responses']:
        if index < k:
            answer_set[i['zheng_hou_name']] = i['description']
            index = index + 1
    try:
        res = json.loads(llm_data["answer"].replace('```json\n','').replace('\n```','').replace('```\n','').replace("'", '"'))
    except Exception:
        logger.exception("转换LLM回答出错")
        return 0.0
    if isinstance(res, dict):
        res = [res]
    try:
        res = sorted(res, key=lambda x: float(x['gai_lv'].strip('%')), reverse=True)
    except Exception:
        logger.exception(f"data: {res}")
    score = 0
    j = 0
    for i in res:
        if j > k:
            break
        try:
            if i['zheng_hou_name'] in answer_set:
                score += 0.5
                score = score + bert_scoring(answer_set[i['zheng_hou_name']], i['description']) / 2
        except:
            logger.exception("")
        j += 1
    return score / k
