import argparse
import importlib
import os.path

from make_answer.chat import name_model_dict
from make_answer.chat.api_llm_workers import LlmApiWorkers
from make_answer.chat.chat_invoker import ChatInvoker
from make_answer.chat.local_llm_workers import LlmLocalWorkers
from make_answer.main_answer import chat_process


def parse_args():
    parser = argparse.ArgumentParser(
        description='TCM Assessment Benchmarks by \u7d2b\u613f\u5c3d\u597d')  # 使用argparse解析命令行参数，获取输入文件路径、模型名称、进程数量
    parser.add_argument("--step-chat", type=str, help="run get answer from LLM")
    parser.add_argument('--local-model', type=str, help='Local model absolute path')
    parser.add_argument("--model-type", type=str, help=f"Model type must in {list(name_model_dict.keys())}")
    parser.add_argument('--num-gpus', type=str, default="0", help='Number of GPUs to use')
    parser.add_argument("--api-model", type=str, help="API model, need input model class name. The module in which the API model class resides, Must be inherited from ChatInvoker. Example module.class")
    parser.add_argument("--llm-name", type=str, help="API model name")
    parser.add_argument("--base-url", type=str, help="API base url")
    parser.add_argument("--api-key", type=str, help="API key")
    parser.add_argument("--step-evaluate", type=str, help="run get score from answer, must set answer file path")
    parser.add_argument("--standard-answer-root", type=str, help="standard answer root")
    parser.add_argument('--num-process', type=int, default=1, help='Number of GPUs to use')
    parser.add_argument("--sleep-time", type=float, default=0, help="sleep time")

    return parser.parse_args()


def step_chat(_args: argparse.Namespace, *args, **kwargs):
    if not os.path.isdir(_args.step_chat):
        raise ValueError(f"Invalid chat file path: {_args.step_chat}, must be a directory")
    if _args.local_model:
        model_type = _args.model_type
        if model_type not in name_model_dict:
            raise ValueError(f"Invalid model type: {model_type}, must be one of {list(name_model_dict.keys())}")
        model_cls = name_model_dict[model_type]
        workers = LlmLocalWorkers()
        workers.init(_args.local_model, model_cls, _args.num_process, _args.num_gpus, _args.sleep_time)
        if _args.local_model.endswith("/"):
            model_name = os.path.basename(_args.local_model[:-1])
        else:
            model_name = os.path.basename(_args.local_model)
    else:
        workers = LlmApiWorkers()
        # 获取最后一个.号的字符
        module_name, cls_name = _args.api_model.rsplit(".", 1)
        module = importlib.import_module(module_name)
        cls = getattr(module, cls_name)
        if not issubclass(cls, ChatInvoker):
            raise TypeError(f"{_args.api_model} must inherit from ChatInvoker")
        model_name = _args.llm_name
        workers.init(
            cls, _args.num_process,
            *args, model_name=model_name,
            base_url=_args.base_url, api_key=_args.api_key, sleep_time=_args.sleep_time,**kwargs)
    chat_process(workers, model_name, _args.step_chat, num_process=_args.num_process)




if __name__ == '__main__':
    args = parse_args()

    if args.step_chat:
        step_chat(args)

