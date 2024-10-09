import json
import os
from concurrent.futures import ThreadPoolExecutor

import tqdm
from loguru import logger

from make_answer.chat.chat_invoker import ChatInvoker
from make_answer.works import question_prompt_dict


def chat_process(
    chat_invoker: ChatInvoker, model_name: str,
    data_root: str, output_root: str = "output", num_process: int = 1
):
    with ThreadPoolExecutor(max_workers=num_process) as executor:
        for data_file in os.listdir(data_root):
            data_path = os.path.join(data_root, data_file)
            logger.info(f"Start process {data_path}")
            output_dir = os.path.join(output_root, model_name, os.path.splitext(data_file)[0])
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            mid_file = os.path.join(output_dir, "mid.jsonl")
            line_count = 0
            if os.path.exists(mid_file):
                with open(mid_file, encoding="utf-8") as f:
                    line_count = sum(1 for _ in f)
                if line_count:
                    logger.info(f"Find {line_count} lines, skip")
            data_lines = []
            total_count = 0
            with open(data_path, encoding="utf-8") as f:
                for i, line in enumerate(f):
                    total_count += 1
                    if i < line_count:
                        continue
                    data_lines.append(json.loads(line))
            process_bar = tqdm.tqdm(total=total_count, desc=f"{data_file} use {model_name} Process", unit="line")
            if line_count:
                process_bar.update(line_count)
            if data_file[0].isalpha():
                work_func = question_prompt_dict[data_file[0]]
            else:
                work_func = question_prompt_dict[data_file.split(".")[0]]
            if data_lines:
                for data in executor.map(
                    work_func, data_lines, [chat_invoker] * len(data_lines)
                ):
                    process_bar.update()
                    with open(mid_file, "a", encoding="utf-8") as f:
                        f.write(json.dumps(data, ensure_ascii=False))
                        f.write("\n")
            process_bar.close()

