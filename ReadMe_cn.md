# CTCMB 中医综合评估基准 

<center>

![Python 3.12](https://img.shields.io/badge/Python-3.12-lightblue) ![Torch 2.3.1](https://img.shields.io/badge/PyTorch-2.3.1-lightblue) ![OpenAi 1.25.0](https://img.shields.io/badge/openai-1.25.0-lightblue) ![bert-score](https://img.shields.io/badge/bert--score-0.3.13-lightblue)
</center>

![title](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/pics/title.jpg)

<p align="center">
   📃 <a href="" target="_blank">Paper</a> • 🌐 <a href="" target="_blank">Website</a>  
   <br>  <a href="https://github.com/TrustedGPT/CTCMB/blob/main/ReadMe_cn.md">   中文</a> | <a href="https://github.com/TrustedGPT/CTCMB/blob/main/ReadMe.md"> English
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


| 模型名称                   | 中医知识问答 | 医学语言生成 | 中医语言理解 | 中医诊断 | 中医推理 | 中医平均分 | 名次 |
| -------------------------- | ------------ | ------------ | ------------ | -------- | -------- | ---------- | ---- |
| ERNIE-4.0-8k-Latest        | 66.58        | 59.80        | 71.12        | 65.46    | 68.00    | 65.71      | 1    |
| hunyuan-pro                | 70.06        | 60.74        | 72.35        | 60.02    | 65.50    | 65.01      | 2    |
| step-2-16k-nightly         | 64.43        | 61.41        | 72.99        | 63.91    | 66.50    | 64.89      | 3    |
| qwen2-72b-instruct         | 68.52        | 59.27        | 72.92        | 61.69    | 65.00    | 64.73      | 4    |
| gemini-1.5-pro             | 61.71        | 69.5         | 72           | 63.97    | 61.3     | 64.6       | 5    |
| glm-4-0520                 | 66.67        | 60.76        | 69.74        | 58.39    | 67.00    | 63.68      | 6    |
| tiangong                   | 70.23        | 59.98        | 69.49        | 60.81    | 58.00    | 63.51      | 7    |
| SenseChat-5                | 64.14        | 59.70        | 74.36        | 56.92    | 69.50    | 63.27      | 8    |
| Llama-3.1-405b             | 62.00        | 61.35        | 73.97        | 55.09    | 68.00    | 62.18      | 9    |
| 360gpt2-pro                | 68.37        | 57.75        | 73.96        | 53.30    | 64.50    | 62.13      | 10   |
| moonshot-v1-8k             | 58.98        | 61.93        | 70.05        | 58.79    | 63.00    | 61.2       | 11   |
| abab6.5s-chat-pro          | 59.03        | 62.01        | 71.84        | 52.79    | 68.50    | 60.76      | 12   |
| deepseek-chat              | 63.30        | 62.41        | 71.18        | 57.05    | 53.00    | 60.28      | 13   |
| Baichuan4                  | 60.20        | 58.11        | 72.66        | 59.56    | 56.00    | 60.01      | 14   |
| claude-3-5-sonnet-20240620 | 54.06        | 63.40        | 53.88        | 59.05    | 62.50    | 58.64      | 15   |
| gpt-4-turbo-2024-04-09     | 54.65        | 61.33        | 72.68        | 52.33    | 59.00    | 57.66      | 16   |
| gemini-pro                 | 50.39        | 63.61        | 65.70        | 51.15    | 67.50    | 57.5       | 17   |
| Doubao-pro-4k              | 59.17        | 57.83        | 67.53        | 53.64    | 50.50    | 56.6       | 18   |
| mistral-large-latest       | 51.79        | 62.62        | 73.19        | 50.02    | 58.00    | 56.35      | 19   |
| yi-large-turbo             | 58.38        | 57.05        | 60.95        | 51.03    | 56.50    | 56.03      | 20   |
| Spark4.0 Ultra             | 48.90        | 62.46        | 64.82        | 44.77    | 48.50    | 51.61      | 21   |
| Taiyi-7B                   | 52.61        | 47.5         | 71           | 41.07    | 30.88    | 46.25      | 22   |
| WiNGPT2-14B-Chat           | 52.2         | 53           | 58           | 53.67    | 11.53    | 45.88      | 23   |
| HuatuoGPT2-34B             | 45.1         | 57.5         | 58           | 38.27    | 23       | 42.65      | 24   |
## 😊数据集描述

![pie-nest](https://github.com/Wayyuanyuan/CTCMB/blob/main/pics/line-simple.png)

#### 结构

数据集：**5**个类别，**11**个数据集

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
|              | [TCM-DID](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/3.TCM-DID%20Dataset.md) | 100  | 《中医基础理论习题集》主编郑洪新                             | 使用Bertscore                       |
|              | [TCM-FT](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/4.TCM-FT.md)                                                      | 100  | 《中医学问答题库》胡熙明主编                                 | 使用Bertscore                       |
| 医学语言生成 | [TCMeEE](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/8.TCMeEE.md) | 100  | 原始数据是[zhongyigen.com](https://zhongyigen.com/)的医案，利用GPT进行实体抽取，生成而来的。 | 采用Bertscore,ROUGE,BLEU平均的方式 |
|              | [TCM-CHGD](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/5.TCM-CHGD.md) | 100  | 中医智库的医案转化成的对话数据，经gpt转化生成病例            | 采用Bertscore,ROUGE,BLEU平均的方式 |
| 中医推理     | [TCM-SRT](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/10.TCM-SRT.md) | 100  | 来自[CCKS2024-TCMBench](https://tianchi.aliyun.com/competition/entrance/532204label)中医知识理解与推理能力评测中任务二的数据。 | Accuracy                             |
|              | [SPD](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/12.SPD.md) | 100  | GPT生成结合《中医临床诊疗术语-第2部分：证候》的数据生成生成而来 | Top-k方法                            |
| 中医语言理解 | [TCM-LitData](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/9.TCM-LitData.md) | 100  | 来自[网站](https://tianchi.aliyun.com/dataset/86895)的中医文献问题生成数据集。 | 采用Bertscore,ROUGE,BLEU平均的方式 |
| 中医诊断     | [Med-Treat](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/6.Med-Treat.md) | 100  | 从中医方剂网爬取的数据转化而来。                             | 采用Bertscore,ROUGE,BLEU平均的方式 |
|              | [TCM-Clin](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/7.TCM-Clin.md) | 100  | [A Benchmark for Probing Syndrome Differentiation via Natural Language Processing](https://arxiv.org/abs/2203.10839) 文章的数据。 | 使用Bertscore                       |
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
python main.py --step-chat data --api-model make_answer.chat.remote.openai_api.LlmOpenai --llm-name your_model_name  --base-url your_url --api-key your_key --num-process 12
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
--model-type LLM名称 # 大模型名称，需要将自定模版构造函数写在：make_answer/chat/__init__.py的name_model_dict中。
```

##### 一个示例

```
python main.py --step-chat data/ --local-model  /mnt/data1/MedLLM_baselines/Taiyi --model-type taiyi
```



## 提交格式要求



我们的评估基准包括11个数据集，每个数据集包含若干个题目，这些题目的answer字段为空。一个简短的示例如下：

```
{"question": "何谓血瘀?血瘀是如何形成的?", "answer": ""}
{"question": "肾“其华在发”有何理论依据?", "answer": ""}
{"question": "奇经八脉有何主要生理功能?", "answer": ""}
```

我们的评估代码要求接受下面的数据格式，

```
{"question": "何谓血瘀?血瘀是如何形成的?", "answer": "血瘀是指血液运行不畅、停滞于血脉之中而形成的一种病理状态。其主要表现为皮肤出现青紫斑块、疼痛等症状。血瘀的形成原因包括外伤、情绪波动等因素，也与体内气虚、阳虚等内在因素有关。治疗上应以活血化瘀为主，可采用针灸、中药等方式进行调理。"}
{"question": "肾“其华在发”有何理论依据?", "answer": "《黄帝内经》中记载：“人之五脏六腑、四肢百骸皆禀于自然，而血气亦各有所主。心藏神，肺藏魄，肝藏魂，脾藏意，肾藏志，此五者，皆藏于精。”其中，“肾藏志”，即指肾脏所藏之精神意志。“其华在发”，则说明肾脏的精神状态反映在外表上，即头发的状态。因此，从中医的角度来看，肾“其华在发”的理论依据是《黄帝内经》中的“五脏六腑、四肢百骸皆禀于自然，而血气亦各有所主。心藏神，肺藏魄，肝藏魂，脾藏意，肾藏志，此五者，皆藏于精。”这一理论认为，人体的各种生理功能都与五脏有关，而头发的状态则是由肾脏所支配的。因此，肾脏的精神状态可以通过头发来表现出来。"}
{"question": "奇经八脉有何主要生理功能?", "answer": "奇经八脉是中医学中的重要理论之一，其主要生理功能包括调节全身气血运行、维持脏腑功能平衡、促进人体阴阳协调等方面。其中，任督二脉是奇经八脉的核心，通过调节心肾之间的水火相济关系，达到调和阴阳、平衡气血的目的；而冲任二脉则与女性生殖系统密切相关，可以调节月经、孕育胎儿等生理过程；带脉则是人体腹部的一条横行脉络，具有固护腰腹、调节脾胃等功能；阴维脉则为人体阴气的主要通道，可以调节人体阴液的，维持人体阴液的正常代谢；阳维脉则为人体阳气的主要通道，可以调节人体阳气的正常代谢。总之，奇经八脉在人体内发挥着重要的生理作用，对人体健康有着不可忽视的影响。"}
```

本质上是将answer字段使用模型的回答进行填充。这些的数据被保存在mid.jsonl文件中。

我们拥有11个数据集，我们期待采用以下的命名方式提交

```
一级目录 （模型名）
├── A_problem
│   └── mid.jsonl
├── B_problem
│   └── mid.jsonl
├── C_problem
│   └── mid.jsonl
├── D_problem
│   └── mid.jsonl
├── 2.TCM-DS Dataset
│   └── mid.jsonl
├── 3.TCM-DID Dataset
│   └── mid.jsonl
├── 4.TCM-FT
│   └── mid.jsonl
├── 5.TCM-CHGD
│   └── mid.jsonl
├── 6.Med-Treat
│   └── mid.jsonl
├── 7.TCM-Clin
│   └── mid.jsonl
├── 8.TCMeEE
│   └── mid.jsonl
├── 9.TCM-LitData
│   └── mid.jsonl
├── 10.TCM-SRT
│   └── mid.jsonl
└── 12.SPD
    └── mid.jsonl
```

你需要采用压缩包的方式提交。比如 gemini-1.5-pro.zip

   1. 你需要点击“选择文件”按钮，选择本地的压缩包文件。 
   2. 点击“上传并处理”按钮，通常需要30-60min钟即可对答案进行评分。
   3. 处理完成后，你可以点击“下载评估结果”按钮下载评估结果。
   4. 可以将结果分数发送至xxx@163.com进行宣传。


## 致谢


我们衷心感谢×××对本项目的巨大支持。🎉🎉🎉

同时，感谢参与本项目的全体成员！

