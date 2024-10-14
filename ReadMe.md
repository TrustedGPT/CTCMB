# CTCMB 中医综合评估基准 

<center>

![Python 3.12](https://img.shields.io/badge/Python-3.12-lightblue) ![Torch 2.3.1](https://img.shields.io/badge/PyTorch-2.3.1-lightblue) ![OpenAi 1.25.0](https://img.shields.io/badge/openai-1.25.0-lightblue) ![bert-score](https://img.shields.io/badge/bert--score-0.3.13-lightblue)
</center>

![title](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/pics/title.jpg)

<p align="center">
   📃 <a href="" target="_blank">Paper</a> • 🌐 <a href="" target="_blank">Website</a>  
   <br>  <a href="">   中文</a> | <a href=""> English
</p>



## 🌈 更新

- **[2024.××.××]** 论文被××接受，感谢学术界对其的认可。
- **[2024.××.××]** 发布了论文。
- **[2024.××.××]** 🎉🎉🎉 CTCMB 正式发布！🎉🎉🎉
## 🌐 数据下载

（1）Zip格式

```python
git clone "https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks.git"&& cd TCM-Assessment-Benchmarks/data
```

（2）[百度云链接](https://pan.baidu.com/s/1T91QMVJJR7IfkIoL6KCdGA?pwd=3iu2)



## 📍排行榜​​

| 模型名称                   | TCM-ED | TCM-DS | TCM-DID | TCM-FT | TCM-GHGD | Med-Treat | TCM-Clin | TCMeEE | TCM-LitData | TCM-SRT | SPD   | 平均分 | 名次 |
| -------------------------- | ------ | ------ | ------- | ------ | -------- | --------- | -------- | ------ | ----------- | ------- | ----- | ------ | ---- |
| 仲思-34b-v1 (ours)         | 86.15  | 83.75  | 59.00   | 72.00  | 54.00    | 50.00     | 92.00    | 84.00  | 72.00       | 99.00   | 57.85 | 73.61  | 1    |
| ERNIE-4.0-8k-Latest        | 72.25  | 68.00  | 54.77   | 72.73  | 60.23    | 59.61     | 68.78    | 59.37  | 71.12       | 88.00   | 48.00 | 65.71  | 2    |
| hunyuan-pro                | 75.50  | 51.00  | 62.63   | 72.06  | 60.41    | 59.54     | 69.52    | 61.08  | 72.35       | 81.00   | 50.00 | 65.01  | 3    |
| step-2-16k-nightly         | 67.00  | 60.00  | 54.49   | 71.79  | 58.60    | 56.07     | 75.67    | 64.22  | 72.99       | 89.00   | 44.00 | 64.89  | 4    |
| qwen2-72b-instruct         | 81.00  | 60.00  | 53.39   | 71.16  | 56.76    | 52.32     | 72.75    | 61.77  | 72.92       | 84.00   | 46.00 | 64.73  | 5    |
| gemini-1.5-pro             | 68.13  | 67.90  | 47.00   | 70.00  | 62.00    | 51.00     | 73.00    | 77.00  | 72.00       | 86.00   | 36.60 | 64.60  | 6    |
| glm-4-0520                 | 71.25  | 54.00  | 56.75   | 72.02  | 60.77    | 52.53     | 68.65    | 60.74  | 69.74       | 93.00   | 41.00 | 63.68  | 7    |
| tiangong                   | 86.00  | 57.00  | 54.34   | 70.35  | 59.37    | 52.81     | 72.63    | 60.58  | 69.49       | 76.00   | 40.00 | 63.51  | 8    |
| SenseChat-5                | 67.75  | 49.00  | 53.28   | 71.39  | 58.57    | 54.82     | 66.95    | 60.83  | 74.36       | 89.00   | 50.00 | 63.27  | 9    |
| Llama-3.1-405b             | 64.25  | 40.00  | 50.98   | 70.77  | 58.28    | 49.36     | 75.92    | 64.42  | 73.97       | 84.00   | 52.00 | 62.18  | 10   |
| 360gpt2-pro                | 75.50  | 40.00  | 57.97   | 71.63  | 55.04    | 51.75     | 68.15    | 60.46  | 73.96       | 81.00   | 48.00 | 62.13  | 11   |
| moonshot-v1-8k             | 59.50  | 51.00  | 46.27   | 71.16  | 61.76    | 49.58     | 75.79    | 62.09  | 70.05       | 90.00   | 36.00 | 61.20  | 12   |
| abab6.5s-chat-pro          | 58.00  | 47.00  | 48.28   | 70.81  | 63.70    | 43.36     | 68.01    | 60.33  | 71.84       | 85.00   | 52.00 | 60.76  | 13   |
| deepseek-chat              | 70.25  | 54.00  | 48.35   | 71.30  | 56.49    | 52.77     | 64.39    | 68.32  | 71.18       | 70.00   | 36.00 | 60.28  | 14   |
| Baichuan4                  | 63.75  | 60.00  | 47.18   | 69.67  | 66.62    | 50.44     | 68.23    | 49.59  | 72.66       | 87.00   | 25.00 | 60.01  | 15   |
| claude-3-5-sonnet-20240620 | 46.75  | 52.00  | 45.87   | 69.56  | 61.74    | 49.80     | 75.36    | 65.07  | 53.88       | 87.00   | 38.00 | 58.64  | 16   |
| gpt-4-turbo-2024-04-09     | 47.25  | 36.00  | 47.21   | 69.50  | 62.23    | 46.31     | 74.67    | 60.42  | 72.68       | 78.00   | 40.00 | 57.66  | 17   |
| Doubao-pro-4k              | 62.75  | 38.00  | 42.23   | 72.52  | 57.16    | 55.78     | 67.15    | 58.51  | 67.53       | 56.00   | 45.00 | 56.60  | 18  |
| mistral-large-latest       | 37.25  | 36.00  | 47.55   | 70.57  | 60.30    | 46.47     | 67.59    | 64.94  | 73.19       | 70.00   | 46.00 | 56.35  | 19   |
| yi-large-turbo             | 53.75  | 38.00  | 50.91   | 70.48  | 56.46    | 48.22     | 66.87    | 57.65  | 60.95       | 68.00   | 45.00 | 56.03  | 20   |
| Spark4.0 Ultra             | 35.25  | 24.00  | 41.02   | 70.43  | 64.43    | 46.22     | 64.08    | 60.49  | 64.82       | 83.00   | 14.00 | 51.61  | 21   |
| Taiyi                      | 42.83  | 17.20  | 47.00   | 68.00  | 42.00    | 45.00     | 61.00    | 53.00  | 71.00       | 58.00   | 3.76  | 46.25  | 22   |
| WiNGPT2-14B-Chat           | 53.60  | 52.00  | 35.00   | 68.00  | 49.00    | 45.00     | 64.00    | 57.00  | 58.00       | 21.00   | 2.06  | 45.88  | 23   |
| HuatuoGPT2-34B             | 29.30  | 25.80  | 39.00   | 67.00  | 55.00    | 25.00     | 64.00    | 60.00  | 58.00       | 45.00   | 1.00  | 42.65  | 24   |

## 😊数据集描述

![pie-nest](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/pics/pie-nest.png)

#### 结构

数据集：**5**个类别，**12**个数据集

5个类别（每个类别包含1-3个数据集）

- 中医知识问答：以选择、判断和问答形式考核中医基础。
- 医学语言生成：评估模型生成标准医学文本的能力。
- 中医推理：评估模型基于中医理论的推理能力。
- 中医语言理解：评估模型对中医专业语言的理解。
- 中医诊断：评估模型运用四诊合参的诊断能力。

TCM-ED  TCM-DS  TCM-SRT 为客观题,其余为主观题，其中TCM-ED包含A型题（最佳选择题）、B型题（病历摘要型最佳选择题）、C型题（共用题干选择题）以及D型题（共用选项选择题）。

#### 详细信息

**点击超链接可以查看到不同数据集格式要求**⬅️⬅️

| 一级目录     | 二级目录                                                     | 数量 | 数据来源                                                     | 评估方法                             |
| :----------- | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ | ------------------------------------ |
| 中医知识问答 | TCM-ED（[A](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/A_problem.md)、[B](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/B_problem.md)、[C](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/C_problem.md)、[D](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/D_problem.md)） | 720  | ACD来自中医主治医师考核和职业医师考核，B是GPT生成            | Accuracy                             |
|              | [TCM-DID](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/3.TCM-DID%20Dataset.md) | 100  | 《中医基础理论习题集》主编郑洪新                             | 使用BERTScoing                       |
|              | [TCM-FT](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/4.TCM-FT.md)                                                      | 100  | 《中医学问答题库》胡熙明主编                                 | 使用BERTScoing                       |
| 医学语言生成 | [TCMeEE](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/8.TCMeEE.md) | 100  | 原始数据是[zhongyigen.com](https://zhongyigen.com/)的医案，利用GPT进行实体抽取，生成而来的。 | 采用BERTScoring,ROUGE,BLEU平均的方式 |
|              | [SCD](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/11.SCD.md) | 100  | 使用医案生成病历数据，然后再将病例进行切分，切分后的病例分别用于生成原对话和补充对话，再利用原对话生成原始的现病史和既往史，将未切分的病例作为调优的现病史和既往史。 | LLM评估                              |
|              | [TCM-CHGD](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/5.TCM-CHGD.md) | 100  | 中医智库的医案转化成的对话数据，经gpt转化生成病例            | 采用BERTScoring,ROUGE,BLEU平均的方式 |
| 中医推理     | [TCM-SRT](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/10.TCM-SRT.md) | 100  | 来自[CCKS2024-TCMBench](https://tianchi.aliyun.com/competition/entrance/532204label)中医知识理解与推理能力评测中任务二的数据。 | Accuracy                             |
|              | [SPD](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/12.SPD.md) | 100  | GPT生成结合《中医临床诊疗术语-第2部分：证候》的数据生成生成而来 | Top-k方法                            |
| 中医语言理解 | [TCM-LitData](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/9.TCM-LitData.md) | 100  | 来自[网站](https://tianchi.aliyun.com/dataset/86895)的中医文献问题生成数据集。 | 采用BERTScoring,ROUGE,BLEU平均的方式 |
| 中医诊断     | [Med-Treat](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/6.Med-Treat.md) | 100  | 从中医方剂网爬取的数据转化而来。                             | 采用BERTScoring,ROUGE,BLEU平均的方式 |
|              | [TCM-Clin](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/7.TCM-Clin.md) | 100  | [A Benchmark for Probing Syndrome Differentiation via Natural Language Processing](https://arxiv.org/abs/2203.10839) 文章的数据。 | 使用BERTScoing                       |
|              | [TCM-DS](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/2.TCM-DS%20Dataset.md) | 200  | GPT根据《中医临床诊疗术语-第2部分：证候》中对疾病的描述生成。 | Accuracy                             |





## 🔆如何提交和评估

### 环境配置


确保你的开发环境已经安装了[文件](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/requirements.txt)要求的Python库





### 问答模块

目前提供基于OpenAI库的调用模版，并且提供三套HuggingFace上开源库的调用模版，分别是`HuatuoGPT-II`，`Taiyi-LLM`和`WiNGPT2`调用。如果需要其他更多调用的支持，请继承自`make_answer/chat/chat_invoker.py`模块中的`ChatInvoker`接口。

#### 基于OpenAI库的调用模版

`模块名.调用llm文件`.py


```python
import os
import openai

from loguru import logger
from make_answer.chat.chat_invoker import ChatInvoker


class LlmOpenai(ChatInvoker):
    def __init__(self, *args, **kwargs):
        base_url = os.environ.get("OPENAI_BASE_URL")
        if "base_url" in kwargs:
            base_url = kwargs["base_url"]
        api_key = os.environ.get("OPENAI_API_KEY")
        if "api_key" in kwargs:
            api_key = kwargs["api_key"]
        self.client = openai.OpenAI(
            base_url=base_url, api_key=api_key)
        self.model_name = kwargs["model_name"]

    def chat(self, msg: str, *args, **kwargs) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "你是一个专业中医医生，能够准确全面的解答中医问题。本次对话，均只采用中文提问和回答。"},
                {"role": "user", "content": msg}
            ]
        )
        try:
            ret = response.choices[0].message.content
        except Exception as e:
            logger.exception(f"call openai chat api error: {response}")
            raise e

        return ret
```

##### 使用方式

```python
python main.py \
--step-chat data/ \ # 测试问题所在文件夹
--api-model 模块名.调用llm文件.类名 \ # 自定义测试模型，需要继承自ChatInvoker，传入完整模块名、文件名和类名
--api-model-name 调用的大模型名称 \ # 大模型名称，用于区分调用的不同模型，以及不同模型结果
--base-url 模型调用url \ # 模型url
--api-key 模型key  # 调用模型key
```

##### 基于OpenAI库的调用示例

```
python main.py --step-chat data --api-model make_answer.chat.remote.openai_api.LlmOpenai --llm-name your_model_name  --base-url your_url --api-key your——key --num-process 12
```



#### 基于本地调用形式

`模块名.调用llm文件`.py

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from make_answer.chat.chat_invoker import ChatInvoker


class LocalLLM(ChatInvoker):
    def __init__(self, model_path: str, gpu_id: int = 0):
        # 模型初始化，仅在首次运行时执行。

    def chat(
            self, msg: str, *args, **kwargs
    ) -> str:
        # 请求模型回答，msg为必填参数。
```

##### 使用方式

```python
python main.py \
--step-chat data/ \ # 测试问题所在文件夹
--local-model /Path/To/LLM \ # 本地大模型所在目录
--chat-func-name LLM名称 # 大模型名称，需要将自定模版构造函数写在：make_answer/chat/__init__.py的name_model_dict中。
```



### 评估模块

使用方式

```python
python main.py \
--step-evaluate LLM回答所在目录 \ # 一般情况下， 传入根目录下模型名称
--standard-answer-root 标准答案目录 # 传入标准答案目录
```



### 其他参数

 

| 参数名称      | 默认值 | 作用                               |
| ------------- | ------ | ---------------------------------- |
| --num-process | 1      | 调用大模型回答以及评估时并发线程数 |
| --sleep-time  | 0      | 大模型单次回答后，等待的时间。     |





## 致谢


我们衷心感谢×××对本项目的巨大支持。🎉🎉🎉

同时，感谢参与本项目的全体成员！


