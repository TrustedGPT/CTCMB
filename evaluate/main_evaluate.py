import glob
import json
import os.path
from concurrent.futures.thread import ThreadPoolExecutor

import pandas as pd
import tqdm

from loguru import logger

from evaluate.works import question_standard_dict


def evaluate_process(
    standard_answer_root: str, chat_answer_root: str, *args, **kwargs
):
    for chat_answer_file in glob.glob(chat_answer_root + "/**/mid.jsonl", recursive=True):
        if not os.path.isfile(chat_answer_file) or os.path.splitext(chat_answer_file)[1] != ".jsonl":
            continue
        chat_answer_kind = os.path.basename(os.path.dirname(chat_answer_file))
        output_dir = os.path.dirname(chat_answer_file)
        output_file = os.path.join(output_dir, "score.json")
        if os.path.exists(output_file):
            logger.info(f"Already evaluate {chat_answer_kind}, skip")
            continue
        standard_answer_file = os.path.join(standard_answer_root, chat_answer_kind + '.jsonl')
        if not os.path.isfile(standard_answer_file):
            logger.error(f"Can not find standard answer file {standard_answer_file}")
            continue
        logger.info(f"File({chat_answer_file}) use standard answer file({standard_answer_file})")
        if chat_answer_kind[0].isalpha():
            work_func = question_standard_dict[chat_answer_kind[0]]
        else:
            work_func = question_standard_dict[chat_answer_kind.split(".")[0]]
        with open(chat_answer_file, encoding="utf8") as f:
            chat_answer_data = [json.loads(line) for line in f]
        with open(standard_answer_file, encoding="utf8") as f:
            standard_answer_data = [json.loads(line) for line in f]

        if len(chat_answer_data) != len(standard_answer_data):
            logger.error(f"Data size not match, chat_answer({len(chat_answer_data)}) standard_answer({len(standard_answer_data)})")
            continue
        num_process = kwargs.get("num_process", 1)

        scores = []
        process_bar = tqdm.tqdm(total=len(chat_answer_data), desc=f"{chat_answer_kind} Evaluate", unit="line")
        with ThreadPoolExecutor(max_workers=num_process) as executor:
            for result in executor.map(work_func, standard_answer_data, chat_answer_data):
                scores.append(result)
                process_bar.update(1)

        with open(output_file, "w", encoding="utf8") as f:
            output_data = json.dumps(scores, ensure_ascii=False, indent=4)
            f.write(output_data)
        logger.info(f"Save score to {output_file}")

        if chat_answer_kind in ["A_problem", "B_problem", "C_problem", "D_problem",
                                "10.TCM-SRT", "2.TCM-DS Dataset", "12.SPD","14.CHIP-CTC"]:
            score = sum(scores) / len(scores) * 100
        elif chat_answer_kind in ["3.TCM-DID Dataset", "4.TCM-FT", "7.TCM-Clin"]:
            score = sum([s["bert"] for s in scores if isinstance(s, dict)]) * 100 // len(scores)
        elif chat_answer_kind in ["8.TCMeEE", "5.TCM-CHGD", "9.TCM-LitData", "6.Med-Treat", "16.IMCS-V2-MRG","13.CHIP-CDEE", "15.CMeEE"]:
            score = sum([((s["rouge_1"]*100 + s["rouge_l"]*100) / 2 + s["bert"] *100+ s["bleu"]) / 3
                         for s in scores if isinstance(s, dict)])// len(scores)
        else:
            score = "/"

        # calculate score
        summary_score_df = pd.DataFrame({"question_name": chat_answer_kind, "score": score}, index=[0])

        if os.path.exists(os.path.join(chat_answer_root, "summary_score.xlsx")):
            exists_df = pd.read_excel(os.path.join(chat_answer_root, "summary_score.xlsx"))
            if "question_name" not in exists_df.columns or "question_name" not in summary_score_df.columns:
                raise ValueError(f"Key column 'question_name' does not exist in one of the DataFrames.")
            # 合并两个DataFrame，根据key_column进行外连接（outer join）
            merged_df = pd.merge(exists_df, summary_score_df, on="question_name", how='outer', suffixes=('', '_new'))

            # 更新已有的列，并保留新列
            for col in summary_score_df.columns:
                if col != "question_name":
                    # 使用新的值覆盖旧的值
                    merged_df[col] = merged_df[col + '_new'].combine_first(merged_df[col])
                    # 删除临时的新列
                    if col + '_new' in merged_df.columns:
                        merged_df.drop(columns=[col + '_new'], inplace=True)

            # 保存更新后的DataFrame回到CSV文件
            merged_df.to_excel(os.path.join(chat_answer_root, "summary_score.xlsx"), index=False)
        else:
            summary_score_df.to_excel(os.path.join(chat_answer_root, "summary_score.xlsx"), index=False)
