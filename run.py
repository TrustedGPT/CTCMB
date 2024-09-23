import argparse
import json
import os
from loguru import logger
from typing import Callable, Union

import pandas as pd

from score_func.C_problem import single_c
from score_func.D_problem import single_d
from score_func.Med_Treat_score import med_treat
from score_func.TCM_CHGD_score import tcm_chgd
from score_func.TCM_Clin_score import tcm_clin
from score_func.TCM_DID_Dataset_score import tcm_did
from score_func.TCM_DS_Dataset_score import tcm_ds
from score_func.TCM_FT_score import tcm_ft
from score_func.TCM_LitData_score import tcm_litdata
from score_func.TCM_SRT_score import tcm_srt
from score_func.TCMeEE_score import tcmeee
from score_func.a_problem import single_a
from score_func.b_problem import single_b
from chat.LlmChat import LlmChat
from score_func.SCD_score import scd_score
from score_func.SPD_score import spd_score
from time import sleep

from pandas import Series
from pandas.core.interchange.dataframe_protocol import DataFrame
from sparkai.errors import SparkAIConnectionError


def score(filepath: str, score_fuc: Callable[[dict, LlmChat, str], Union[float, dict]], model: str):
    logger.info(f"[{os.getpid()}] start, process {filepath}")  #记录日志
    with open(filepath, encoding="utf8") as f:
        data = json.load(f)
    llm = LlmChat(model)  #初始化LlmChat对象
    file_basename_without_ext = os.path.splitext(os.path.basename(filepath))[0]  # 返回文件名而不包含扩展名
    output_dir = os.path.join("output", model.replace(":", "."), file_basename_without_ext)  # 创建输出文件的完整路径 output/modelname/A_problem/score.txt
    os.makedirs(output_dir, exist_ok=True, mode=0o744)
    mid_file = os.path.join(output_dir, "mid.jsonl")
    output_file = os.path.join(output_dir, "score.txt")
    #with ThreadPoolExecutor(max_workers=1) as executor:   #打开线程池并发执行评分函数 score——fuc
        #scores.extend(executor.map(score_fuc, data, [llm] * len(data), [model]*len(data)))
    if os.path.exists(mid_file):
        with open(mid_file, encoding="utf-8") as f:
            processed_data: DataFrame = pd.read_json(f, lines=True)
    else:
        processed_data: DataFrame = pd.DataFrame()
    logger.info(f"Start from {processed_data.shape[0]} lines")
    for i in data[processed_data.shape[0]:]:
        try:
            score_data = score_fuc(i, llm, model)
            if isinstance(score_data, float):
                score_data = {"%score%": score_data}
            processed_data = pd.concat([processed_data, pd.DataFrame([score_data])], ignore_index=True)
            with open(mid_file, "a", encoding="utf-8") as f:
                json.dump(score_data, f, ensure_ascii=False)
                f.write("\n")
        except SparkAIConnectionError:
            logger.exception("SparkAIConnectionError")
            # 插入一个空数据
            if processed_data.shape[0] > 0:
                last_data: Series = processed_data.iloc[-1]
                last_data_dict: dict = last_data.copy().to_dict()
                if isinstance(last_data_dict["%score%"], float):
                    last_data_dict = {"%score%": 0}
                for k, v in last_data_dict.items():
                    last_data_dict[k] = 0.0
                processed_data = pd.concat([processed_data, pd.DataFrame([last_data_dict])], ignore_index=True)
            else:
                processed_data = pd.concat([processed_data, pd.DataFrame([{"%score%": 0}])], ignore_index=True)
        sleep(5)
    logger.info(f"[{os.getpid()}] end, process {filepath}")   #记录处理结束的日志
    #with open(output_file, "w", encoding="utf-8") as f:      #以写模式打开输出文件，并用UTF-8编码
        #json.dump(scores, f, ensure_ascii=False, indent=2)    #将scores数据写入文件f中，格式为json
    scores: list
    if "%score%" in processed_data.columns:
        scores = processed_data["%score%"].tolist()
    else:
        scores = processed_data.to_dict(orient="records")
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(scores, f, ensure_ascii=False, indent=2)
        logger.info(f"Scores for {filepath} written to {output_file}")
    except Exception as e:
        logger.error(f"Error writing scores to {output_file}: {e}")

if __name__ == '__main__':

    score_func_map = {   #将问题ID映射到对应的评分函数
        "1.3":single_c,"1.4":single_d,"9": tcm_litdata,"1.1":single_a,"1.2":single_b,"2": tcm_ds, "3": tcm_did, "4": tcm_ft, "5": tcm_chgd, "6": med_treat,
        "7": tcm_clin, "8": tcmeee,"10": tcm_srt,"11":scd_score, "12":spd_score
    }

    parser = argparse.ArgumentParser(description='Run API Model Test')      #使用argparse解析命令行参数，获取输入文件路径、模型名称、进程数量
    parser.add_argument("-i", "--input", type=str, required=True, help="input file path")
    parser.add_argument('-m', '--model', type=str, required=True, help='choose model')
    parser.add_argument('-p', '--process_size', type=int, default=max(1, os.cpu_count() // 4),
                        help=f'Number of processes, type in [1 - {os.cpu_count()}] default is {max(1, os.cpu_count() // 4)}')
    args = parser.parse_args()
    if not os.path.exists("log"):
        os.makedirs("log")
    logger.add(os.path.join("log", "runtime_" + args.model  + "_{time}.log"), enqueue=True)  #配置日志记录
    logger.info(args)
    model = args.model    #从命令行参数传入模型名称
    process_size = args.process_size
    data = pd.read_csv(args.input, header=0, index_col=None, encoding="utf-8", dtype=str)   #读取输入的CSV文件
    for index, row in data.iterrows():   #对CSV文件每一行数据进行处理
        if row["question_id"] not in score_func_map:      #检查question_id是否在score_func_map中
            raise ValueError(f"question_id {row['question_id']} not in score_func_map")
        if not os.path.exists(row["file"]):      #检查文件是否存在
            raise FileNotFoundError(f"{row['file']} not exists")
        score(row["file"], score_func_map[row["question_id"]], model)   #进行评分
