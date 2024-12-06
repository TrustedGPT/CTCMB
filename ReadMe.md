# Comprehensive Traditional Chinese Medicine Evaluation Criteria of CTCMB

<center>

![Python 3.12](https://img.shields.io/badge/Python-3.12-lightblue) ![Torch 2.3.1](https://img.shields.io/badge/PyTorch-2.3.1-lightblue) ![OpenAi 1.25.0](https://img.shields.io/badge/openai-1.25.0-lightblue) ![bert-score](https://img.shields.io/badge/bert--score-0.3.13-lightblue)
</center>

![title](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/pics/title.jpg)

<p align="center">
   📃 <a href="" target="_blank">Paper</a> • 🌐 <a href="" target="_blank">Website</a>  
   <br>  <a href="">   中文</a> | <a href=""> English
</p>



## 🌈 Update

- **[2024.××.××]** We acknowledge with thanks the acceptance of this paper by ××, which reflects the recognition from the academic community.
- **[2024.××.××]** The research article has been released.
- **[2024.××.××]** 🎉🎉🎉The official release of the CTCMB guidelines is hereby announced!🎉🎉🎉
## 🌐 Data Download

（1）ZIP format

```python
git clone "https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks.git"&& cd TCM-Assessment-Benchmarks/data
```

（2）[Baidu Netdisk Link](https://pan.baidu.com/s/1T91QMVJJR7IfkIoL6KCdGA?pwd=3iu2)



## 📍Ranking List


| Model Name                 | TCM Knowledge Q&A | Medical Language Generation | TCM Language Understanding | TCM Diagnosis | TCM Reasoning | TCM Average Score | Rank |
| -------------------------- | ----------------- | --------------------------- | -------------------------- | ------------- | ------------- | ----------------- | ---- |
| ERNIE-4.0-8k-Latest        | 66.58             | 59.80                       | 71.12                      | 65.46         | 68.00         | 65.71             | 1    |
| hunyuan-pro                | 70.06             | 60.74                       | 72.35                      | 60.02         | 65.50         | 65.01             | 2    |
| step-2-16k-nightly         | 64.43             | 61.41                       | 72.99                      | 63.91         | 66.50         | 64.89             | 3    |
| qwen2-72b-instruct         | 68.52             | 59.27                       | 72.92                      | 61.69         | 65.00         | 64.73             | 4    |
| gemini-1.5-pro             | 61.71             | 69.5                        | 72                         | 63.97         | 61.3          | 64.6              | 5    |
| glm-4-0520                 | 66.67             | 60.76                       | 69.74                      | 58.39         | 67.00         | 63.68             | 6    |
| tiangong                   | 70.23             | 59.98                       | 69.49                      | 60.81         | 58.00         | 63.51             | 7    |
| SenseChat-5                | 64.14             | 59.70                       | 74.36                      | 56.92         | 69.50         | 63.27             | 8    |
| Llama-3.1-405b             | 62.00             | 61.35                       | 73.97                      | 55.09         | 68.00         | 62.18             | 9    |
| 360gpt2-pro                | 68.37             | 57.75                       | 73.96                      | 53.30         | 64.50         | 62.13             | 10   |
| moonshot-v1-8k             | 58.98             | 61.93                       | 70.05                      | 58.79         | 63.00         | 61.2              | 11   |
| abab6.5s-chat-pro          | 59.03             | 62.01                       | 71.84                      | 52.79         | 68.50         | 60.76             | 12   |
| deepseek-chat              | 63.30             | 62.41                       | 71.18                      | 57.05         | 53.00         | 60.28             | 13   |
| Baichuan4                  | 60.20             | 58.11                       | 72.66                      | 59.56         | 56.00         | 60.01             | 14   |
| claude-3-5-sonnet-20240620 | 54.06             | 63.40                       | 53.88                      | 59.05         | 62.50         | 58.64             | 15   |
| gpt-4-turbo-2024-04-09     | 54.65             | 61.33                       | 72.68                      | 52.33         | 59.00         | 57.66             | 16   |
| gemini-pro                 | 50.39             | 63.61                       | 65.70                      | 51.15         | 67.50         | 57.5              | 17   |
| Doubao-pro-4k              | 59.17             | 57.83                       | 67.53                      | 53.64         | 50.50         | 56.6              | 18   |
| mistral-large-latest       | 51.79             | 62.62                       | 73.19                      | 50.02         | 58.00         | 56.35             | 19   |
| yi-large-turbo             | 58.38             | 57.05                       | 60.95                      | 51.03         | 56.50         | 56.03             | 20   |
| Spark4.0 Ultra             | 48.90             | 62.46                       | 64.82                      | 44.77         | 48.50         | 51.61             | 21   |
| Taiyi-7B                   | 52.61             | 47.5                        | 71                         | 41.07         | 30.88         | 46.25             | 22   |
| WiNGPT2-14B-Chat           | 52.2              | 53                          | 58                         | 53.67         | 11.53         | 45.88             | 23   |
| HuatuoGPT2-34B             | 45.1              | 57.5                        | 58                         | 38.27         | 23            | 42.65             | 24   |
## 😊Dataset Description

![pie-nest](https://github.com/Wayyuanyuan/CTCMB/blob/main/pics/line-simple.png)

#### **Data Structure**

The project dataset is structured into **5 categories**, with a total of **11 datasets** available for analysis and research.

- The dataset is divided into **5 categories** (each category containing 1-3 datasets):
  1. **TCM Knowledge Q&A**: Assesses foundational knowledge of TCM through multiple-choice, true/false, and question-and-answer formats.
  2. **Medical Language Generation**: Evaluates the model's ability to generate standardized medical texts.
  3. **TCM Reasoning**: Assesses the model's reasoning capabilities based on Traditional Chinese Medicine theory.
  4. **TCM Language Understanding**: Evaluates the model's comprehension of specialized TCM terminology.
  5. **TCM Diagnosis**: Assesses the model's diagnostic abilities using the four diagnostic methods (inspection, auscultation and olfaction, inquiry, and palpation) in TCM.

TCM-ED, TCM-DS, and TCM-SRT are objective questions, while the rest are subjective questions. Specifically, TCM-ED includes:

- **Type A Questions (Best Choice Questions)**
- **Type B Questions (Case Summary Best Choice Questions)**
- **Type C Questions (Shared Stem Multiple Choice Questions)**
- **Type D Questions (Shared Option Multiple Choice Questions)**

####  Detailed Information

**By clicking the hyperlink, you can access the format requirements for various datasets.**⬅️⬅️

| Primary Catalogues | Secondary Catalogues                                 | Quantity | Data Sources                                         | Evaluation Methods           |
| :----------- | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ | ------------------------------------ |
| TCM Knowledge Q&A | TCM-ED（[A](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/A_problem.md)、[B](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/B_problem.md)、[C](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/C_problem.md)、[D](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/D_problem.md)） | 720  | ACD questions originate from the assessment of certified TCM practitioners and licensed physicians, while type B questions are generated by GPT. | Accuracy                             |
|              | [TCM-DID](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/3.TCM-DID%20Dataset.md) | 100  | Chief Editor Zheng Hongxin, *Exercise Book of Basic Theory of Traditional Chinese Medicine* | Bertscore                 |
|              | [TCM-FT](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/4.TCM-FT.md)                                                      | 100  | Chief Editor Hu Ximing, *Q&A Bank for Traditional Chinese Medicine* | Bertscore                       |
| Medical Language Generation | [TCMeEE](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/8.TCMeEE.md) | 100  | The original data consists of medical cases from [zhongyigen.com](https://zhongyigen.com/). The data was processed using GPT for entity extraction, and the entities were generated accordingly. | Using the average of BERTScore, ROUGE, and BLEU metrics |
|              | [TCM-CHGD](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/5.TCM-CHGD.md) | 100  | Conversation data transformed from medical cases in the TCM Knowledge Base, and subsequently converted into patient cases using GPT. | Using the average of BERTScore, ROUGE, and BLEU metrics |
| TCM Reasoning | [TCM-SRT](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/10.TCM-SRT.md) | 100  | Data from Task 2 of the TCM Knowledge Understanding and Reasoning Evaluation in the [CCKS2024-TCMBench](https://tianchi.aliyun.com/competition/entrance/532204label) competition. | Accuracy                             |
|              | [SPD](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/12.SPD.md) | 100  | Data generated by combining GPT-generated content with terminology from 'Part 2: Patterns' of the *Traditional Chinese Medicine Clinical Diagnosis and Treatment Terms*. | Top-k                            |
| TCM Language Understanding | [TCM-LitData](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/9.TCM-LitData.md) | 100  | TCM Literature Question Generation Dataset from [this website](https://tianchi.aliyun.com/dataset/86895) | Using the average of BERTScore, ROUGE, and BLEU metrics |
| TCM Diagnosis | [Med-Treat](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/6.Med-Treat.md) | 100  | Data transformed from information crawled from the Traditional Chinese Medicine Formula Website. | Using the average of BERTScore, ROUGE, and BLEU metrics |
|              | [TCM-Clin](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/7.TCM-Clin.md) | 100  | Data from the article [A Benchmark for Probing Syndrome Differentiation via Natural Language Processing](https://arxiv.org/abs/2203.10839) | Bertscore                      |
|              | [TCM-DS](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/dataset_info/2.TCM-DS%20Dataset.md) | 200  | Generated by GPT based on the disease descriptions in 'Part 2: Patterns' of the *Traditional Chinese Medicine Clinical Diagnosis and Treatment Terms*. | Accuracy                             |





## 🔆Submission and Evaluation Process

### Environment Configuration


Ensure that your development environment has installed the Python libraries required by the [requirements.txt file](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/requirements.txt).

### Q&A Module

Currently, we provide an invocation template based on the OpenAI library, as well as three invocation templates for open-source libraries on Hugging Face: `HuatuoGPT-II`, `Taiyi-LLM`, and `WiNGPT2`. If you need support for additional invocations, please extend the `ChatInvoker` interface from the `make_answer/chat/chat_invoker.py` module.

#### OpenAI Library-Based Invocation Template

`module_name.call_llm`.py


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

##### Usage

```python
python main.py \
--step-chat data/ \  # Folder containing the test questions
--api-model module_name.call_llm_file.ClassName \  # Custom test model, must inherit from ChatInvoker; provide the full module name, file name, and class name
--api-model-name large_model_name \  # Name of the large model being invoked, used to differentiate between different models and their results
--base-url model_api_url \  # URL for invoking the model
--api-key model_api_key  # API key for invoking the model
```

##### Example of Invocation Using the OpenAI Library

```
python main.py --step-chat data --api-model make_answer.chat.remote.openai_api.LlmOpenai --llm-name your_model_name  --base-url your_url --api-key your_key --num-process 12
```



#### Local Invocation Method

`module_name.call_llm`.py

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from make_answer.chat.chat_invoker import ChatInvoker


class LocalLLM(ChatInvoker):
    def __init__(self, model_path: str, gpu_id: int = 0):
        # Model initialization, which is only performed on the first run.

    def chat(
            self, msg: str, *args, **kwargs
    ) -> str:
        # To request a response from the model, the msg parameter is required.
```

##### Usage Instructions

```python
python main.py \
--step-chat data/ \  # Directory containing the test questions
--local-model /Path/To/LLM \  # Directory where the local large language model (LLM) is located
--model-type LLM_name  # Name of the large language model; the custom template constructor must be written in `make_answer/chat/__init__.py` within the `name_model_dict`.
```

##### Example

```
python main.py --step-chat data/ --local-model  /mnt/data1/MedLLM_baselines/Taiyi --model-type taiyi
```



## Submission Format Requirements



Our evaluation benchmark includes 11 datasets, each containing multiple questions with an empty 'answer' field. A brief example is provided below:

```
{"question": "何谓血瘀?血瘀是如何形成的?", "answer": ""}
{"question": "肾“其华在发”有何理论依据?", "answer": ""}
{"question": "奇经八脉有何主要生理功能?", "answer": ""}
```

Our Evaluation Code Requires the Following Data Format

```
{"question": "何谓血瘀?血瘀是如何形成的?", "answer": "血瘀是指血液运行不畅、停滞于血脉之中而形成的一种病理状态。其主要表现为皮肤出现青紫斑块、疼痛等症状。血瘀的形成原因包括外伤、情绪波动等因素，也与体内气虚、阳虚等内在因素有关。治疗上应以活血化瘀为主，可采用针灸、中药等方式进行调理。"}
{"question": "肾“其华在发”有何理论依据?", "answer": "《黄帝内经》中记载：“人之五脏六腑、四肢百骸皆禀于自然，而血气亦各有所主。心藏神，肺藏魄，肝藏魂，脾藏意，肾藏志，此五者，皆藏于精。”其中，“肾藏志”，即指肾脏所藏之精神意志。“其华在发”，则说明肾脏的精神状态反映在外表上，即头发的状态。因此，从中医的角度来看，肾“其华在发”的理论依据是《黄帝内经》中的“五脏六腑、四肢百骸皆禀于自然，而血气亦各有所主。心藏神，肺藏魄，肝藏魂，脾藏意，肾藏志，此五者，皆藏于精。”这一理论认为，人体的各种生理功能都与五脏有关，而头发的状态则是由肾脏所支配的。因此，肾脏的精神状态可以通过头发来表现出来。"}
{"question": "奇经八脉有何主要生理功能?", "answer": "奇经八脉是中医学中的重要理论之一，其主要生理功能包括调节全身气血运行、维持脏腑功能平衡、促进人体阴阳协调等方面。其中，任督二脉是奇经八脉的核心，通过调节心肾之间的水火相济关系，达到调和阴阳、平衡气血的目的；而冲任二脉则与女性生殖系统密切相关，可以调节月经、孕育胎儿等生理过程；带脉则是人体腹部的一条横行脉络，具有固护腰腹、调节脾胃等功能；阴维脉则为人体阴气的主要通道，可以调节人体阴液的，维持人体阴液的正常代谢；阳维脉则为人体阳气的主要通道，可以调节人体阳气的正常代谢。总之，奇经八脉在人体内发挥着重要的生理作用，对人体健康有着不可忽视的影响。"}
```

Essentially, the 'answer' Field Is Populated with Model Responses. These responses are saved in a file named `mid.jsonl`.

Submission Naming Convention for 11 Datasets. We have 11 datasets, and we expect submissions to follow the naming convention outlined below:

```
Primary Directory (Model Name)
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

You need to submit your files in a compressed package format. For example, gemini-1.5-pro.zip.

1. You need to click the 'Select File' button and choose the compressed file from your local device.
2. Click the 'Upload and Process' button; it usually takes 30-60 minutes to grade the submission.
3. Once processing is complete, you can click the 'Download Evaluation Results' button to download the assessment results.
4. You may send the score results to [xxx@163.com](mailto:xxx@163.com) for promotional purposes.

## Acknowledgments

We would like to extend our heartfelt thanks to XXX for the tremendous support provided to this project. 🎉🎉🎉

Additionally, we appreciate all the members who participated in this project!

