import json

import jieba
import sacrebleu
from bert_score import score
from loguru import logger
from rouge_chinese import Rouge


def bert_scoring(predictions: str, references: str):
    try:
        P, R, F1 = score(cands=[predictions], refs=[references], lang="zh", model_type='bert-base-chinese')
    except Exception:
        logger.exception("Bert score error")
        return 0
    return F1.mean().item()


def rouge1L_scoring(prediction: str, reference: str):
    # 创建 Rouge 对象
    rouge = Rouge()
    # 计算分数
    scores = rouge.get_scores(" ".join(jieba.cut(prediction)), " ".join(jieba.cut(reference)))

    return scores[0]["rouge-1"]["f"], scores[0]["rouge-l"]["f"]



def BLEU(prediction: str, reference: str):
    # 使用 jieba 分词
    prediction_tokens = ' '.join(jieba.cut(prediction))
    reference_tokens = ' '.join(jieba.cut(reference))

    # 使用 sacrebleu 计算 BLEU 分数
    bleu_score = sacrebleu.sentence_bleu(prediction_tokens, [reference_tokens])
    return bleu_score.score

def calculate_micro_f1(true_entities, predicted_entities) -> float:
    """
    计算Micro-F1分数，忽略实体顺序
    参数:
    true_entities - 真实的实体集合，形如 {(entity, type), ...}
    predicted_entities - 模型预测的实体集合，形如 {(entity, type), ...}
    """
    # 将列表中的字典转换为元组集合，元组形式为 (entity, type)
    true_set = set((ent["entity"], ent["type"]) for ent in true_entities)
    predicted_set = set((ent["entity"], ent["type"]) for ent in predicted_entities)

    # 计算TP, FP, FN
    TP = len(true_set & predicted_set)  # 真实和预测中都存在的实体
    FP = len(predicted_set - true_set)  # 预测中存在但真实中不存在的实体
    FN = len(true_set - predicted_set)  # 真实中存在但预测中不存在的实体

    # 计算Precision, Recall, Micro-F1
    if TP + FP == 0:
        precision = 0.0
    else:
        precision = TP / (TP + FP)

    if TP + FN == 0:
        recall = 0.0
    else:
        recall = TP / (TP + FN)

    if precision + recall == 0:
        micro_f1 = 0.0
    else:
        micro_f1 = 2 * precision * recall / (precision + recall)

    return micro_f1

# def calculate_micro_f1_CDEE(true_entities, predicted_entities):
#     # 将列表中的字典转换为元组集合，元组形式为 (entity, type)
#     true_set = set((ent["core_name"], ent["tendency"],tuple(ent["character"]),tuple(ent["anatomy_list"])) for ent in true_entities)
#     predicted_set = set((ent["core_name"], ent["tendency"],tuple(ent["character"]),tuple(ent["anatomy_list"])) for ent in predicted_entities)
#
#     # 计算TP, FP, FN
#     TP = len(true_set & predicted_set)  # 真实和预测中都存在的实体
#     FP = len(predicted_set - true_set)  # 预测中存在但真实中不存在的实体
#     FN = len(true_set - predicted_set)  # 真实中存在但预测中不存在的实体
#
#     # 计算Precision, Recall, Micro-F1
#     if TP + FP == 0:
#         precision = 0.0
#     else:
#         precision = TP / (TP + FP)
#
#     if TP + FN == 0:
#         recall = 0.0
#     else:
#         recall = TP / (TP + FN)
#
#     if precision + recall == 0:
#         micro_f1 = 0.0
#     else:
#         micro_f1 = 2 * precision * recall / (precision + recall)
#
#     return micro_f1
def calculate_micro_f1_CDEE(list_structured_golden, list_structured_predict):
    assert len(list_structured_golden) == len(list_structured_predict)

    tp = 0
    fp = 0
    fn = 0
    for samp_golden, samp_predict in zip(list_structured_golden, list_structured_predict):
        # samp_golden: [[{}]]
        answer_golden = samp_golden
        answer_predict = samp_predict
        # assert isinstance(answer_golden, list)
        # assert isinstance(answer_predict, list), "sample format is wrong!"

        set_golden = set()
        for inst in answer_golden:
            assert isinstance(inst, dict)
            keys = sorted(list(inst.keys()))
            inst = tuple([json.dumps(inst[w], ensure_ascii=False) for w in keys])
            # inst = list(inst.items())
            # inst.sort()
            # inst = tuple(inst)

            set_golden.add(inst)

        set_predict = set()
        for inst in answer_predict:
            assert isinstance(inst, dict)
            keys = sorted(list(inst.keys()))

            inst = tuple([json.dumps(inst[w], ensure_ascii=False) for w in keys])

            set_predict.add(inst)

        tp += len(set_golden.intersection(set_predict))
        fp += len(set_predict.difference(set_golden))
        fn += len(set_golden.difference(set_predict))

    if tp:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1 = 2 * precision * recall / (precision + recall)

    else:
        precision, recall, f1 = 0, 0, 0

    return precision, recall, f1

def multiple_choice_score(prediction: list[str], reference: list[str]):
    """
    选择题得分计算，错选0分，漏选得到选对的分数
    :param prediction:
    :param reference:
    :return:
    """
    prediction = set(prediction)
    reference = set(reference)

    incorrect_choice = prediction - reference
    if len(incorrect_choice) != 0:
        return 0.0
    choice_less = reference - prediction
    return 1.0 - len(choice_less) / len(reference)


def judgement_correction_score(prediction: dict, reference: dict):
    pred_choice = set(prediction["answer"])
    ref_choice = set(reference["answer"])
    pred_reason = prediction["explanation"]
    ref_reason = reference["explanation"]
    if pred_choice != ref_choice:
        return 0.0
    bert=bert_scoring(pred_reason, ref_reason)
    rouge1, rougel = rouge1L_scoring(pred_reason, ref_reason)
    bleu=BLEU(pred_reason,ref_reason)
    return {"rouge1": rouge1, "rouge_l":rougel,"bert":bert,"bleu":bleu}
