## 🌐 数据下载

（1）Zip格式

```python
git clone "https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks.git"&& cd TCM-Assessment-Benchmarks/data
```

（2）[百度云链接](https://pan.baidu.com/s/1T91QMVJJR7IfkIoL6KCdGA?pwd=3iu2)



## 📍排行榜​​

| 模型名称                   | TCM-ED | TCM-DS | TCM-DID | TCM-FT | TCM-GHGD | Med-Treat | TCM-Clin | TCM-eEE | TCM-LitData | TCM-SRT |
| -------------------------- | ------ | ------ | ------- | ------ | -------- | --------- | -------- | ------- | ----------- | ------- |
| 360gpt2-pro                | 75.5   | 40     | 57.97   | 71.63  | 61.28    | 63.63     | 68.15    | 64.35   | 65.38       | 81      |
| gemini-pro                 | 40     | 35     | 41.10   | 70.06  | 46.54    | 52.57     | 72.08    | 57.06   | 60.57       | 83      |
| glm-4-0520                 | 71.25  | 54     | 56.75   | 72.02  | 63.51    | 64.09     | 68.65    | 65.42   | 66.05       | 93      |
| hunyuan-pro                | 75.5   | 51     | 62.63   | 72.06  | 65.30    | 66.66     | 69.52    | 67.16   | 67.78       | 81      |
| Spark4.0 Ultra             | 35.25  | 24     | 41.02   | 70.43  | 42.68    | 51.38     | 64.08    | 52.71   | 56.06       | 83      |
| deepseek-chat              | 70.25  | 54     | 48.35   | 71.3   | 60.98    | 60.21     | 64.39    | 61.86   | 62.15       | 70      |
| qwen2-72b-instruct         | 81     | 60     | 53.39   | 71.16  | 66.39    | 63.65     | 72.75    | 67.59   | 68.00       | 84      |
| ERNIE-4.0-8k-Latest        | 72.25  | 68     | 54.77   | 72.73  | 66.94    | 64.81     | 68.78    | 66.84   | 66.81       | 88      |
| SenseChat-5                | 67.75  | 49     | 53.28   | 71.39  | 60.36    | 61.68     | 66.95    | 62.99   | 63.87       | 89      |
| claude-3-5-sonnet-20240620 | 46.75  | 52     | 45.87   | 69.56  | 53.55    | 56.33     | 75.36    | 61.74   | 64.48       | 87      |
| Doubao-pro-4k              | 62.75  | 38     | 42.23   | 72.52  | 53.88    | 56.21     | 67.15    | 59.08   | 60.81       | 56      |
| gpt-4-turbo-2024-04-09     | 47.25  | 36     | 47.21   | 69.5   | 49.99    | 55.57     | 74.67    | 60.08   | 63.44       | 78      |
| yi-large-turbo             | 53.75  | 38     | 50.91   | 70.48  | 53.29    | 58.23     | 66.87    | 59.46   | 61.52       | 68      |
| Baichuan4                  | 63.75  | 60     | 47.18   | 69.67  | 60.15    | 59.00     | 68.23    | 62.46   | 63.23       | 87      |
| mistral-large-latest       | 37.25  | 36     | 47.55   | 70.57  | 47.84    | 55.32     | 67.59    | 56.92   | 59.94       | 70      |
| moonshot-v1-8k             | 59.5   | 51     | 46.27   | 71.16  | 56.98    | 58.14     | 75.79    | 63.64   | 65.85       | 90      |
| abab6.5s-chat-pro          | 58     | 47     | 48.28   | 70.81  | 56.02    | 58.37     | 68.01    | 60.80   | 62.39       | 85      |
| Llama-3.1-405b             | 64.25  | 40     | 50.98   | 70.77  | 56.50    | 59.42     | 75.92    | 63.95   | 66.43       | 84      |
| step-2-16k-nightly         | 67     | 60     | 54.49   | 71.79  | 63.32    | 63.20     | 75.67    | 67.40   | 68.76       | 89      |

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

- ### **环境配置**


确保你的开发环境已经安装了[文件](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/requirements.txt)要求的Python库

- ###  配置 API 密钥和 URL

在这里，只提供`openai`、`Spart`、`ERNIE`调用方式的配置模版，如果调用模型有其他需求，请按照样例修改。

在使用本项目之前，你需要配置 `api_key` 和 `base_url`。请遵循以下步骤：

1. **创建一个配置文件**：在项目根目录下创建一个名为 `config.py` 的文件，内容如下：

   ```
   # config.py
   API_KEY = "your_api_key_here"
   BASE_URL = "your_base_url_here"
   ```

2. **修改 `LlmChat` 类**：在 `LlmChat` 类中导入配置文件，并使用配置文件中的值替换默认值。

   ```
   from openai import OpenAI
   from ratelimit import limits, sleep_and_retry
   from tenacity import retry, wait_random_exponential, stop_after_attempt
   from loguru import logger
   from config import API_KEY, BASE_URL  # 导入配置文件
   class LlmChat:
       history = []
       
       def __init__(self, model: str = ""):
           self.model = model
           self.client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
   
       def chat(self, msg: str, role_prompt: str = "你是一个专业中医医生，能够准确全面的解答中医问题。本次对话，均只采用中文提问和回答。"):
           messages = [{"role": "system", "content": role_prompt}, {"role": "user", "content": msg}]
           response = self.client.chat.completions.create(model=self.model, messages=messages)
           logger.info(response)
           
           # 检查 response 是否为空或结构异常
           if response and response.choices and response.choices[0].message:
               return response.choices[0].message.content
           else:
               print(f"错误：没有收到有效的响应，消息: {msg}")
               return None
   ```

不同的大模型有不同的 SDK 和 API 接口。你需要根据具体的模型提供商提供的文档来调整你的代码。

#### Spark4.0 Ultra

    from sparkai.core.messages import ChatMessage
    from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
    class LlmChat:
        history = []
    
        def __init__(self, model: str = ""):
            self.model = model
            self.client = ChatSparkLLM(
                spark_api_url="wss://spark-api.xf-yun.com/v4.0/chat",
                spark_app_id="5ef2ecc1",
                spark_api_key="",
                spark_api_secret="",
                spark_llm_domain="4.0Ultra",
                streaming=False,
            )
        def chat(self, msg: str,
                 role_prompt: str = "你是一个专业中医医生，能够准确全面的解答中医问题。本次对话，均只采用中文提问和回答。"):
            messages = [ChatMessage(role="system", content=role_prompt), ChatMessage(role="user", content=msg)]
            handler = ChunkPrintHandler()
            response = self.client.generate([messages], callbacks=[handler])
            if response and response.generations and response.generations[0][0].text:
                return response.generations[0][0].text
            else:
                print(f"错误：没有收到有效的响应，消息: {msg}")
                return None

#### ERNIE-4.0-8K-Latest

```
import qianfan
import os

os.environ["QIANFAN_AK"] = ""
os.environ["QIANFAN_SK"] = ""

class LlmChat:
    history = []

def __init__(self,model: str = ""):
    self.client = qianfan.ChatCompletion()
    self.model_name = model

def chat(self, msg: str,role_prompt: str = "你是一个专业中医医生，能够准确全面的解答中医问题。本次对话，均只采用中文提问和回答。"):
    response = self.client.do(model=self.model_name, messages=[
        {
            "role": "user",
            "content": role_prompt+msg
        }
        ])
    if response["body"]:
        return response["body"]["result"]
    else:
        raise ValueError("Empty response from API")
```

- ### 运行项目


```
#example_input.csv 保存了所有数据集的路径
python run.py -i example_input.csv -m model_name
```

`example_intpu.csv`文件格式要求：`question_id`代表处理不同数据使用的不同评估方法，`file`代表着传入的数据，这些[数据格式](#数据集描述)必须满足超链接中的要求。

完整的`example_input.csv`如下：

```
question_id,file
1.1,data/A_problem.json
1.2,data/B_problem.json
2,data/2.TCM-DS Dataset.json
3,data/3.TCM-DID Dataset.json
4,data/4.TCM-FT.json
5,data/5.TCM-CHGD.json
6,data/6.Med-Treat.json
7,data/7.TCM-Clin.json
8,data/8.TCMeEE.json
10,data/10.TCM-SRT.json
11,data/11.CMeEE.json
12,data/12.CHIP-CTC.json
13,data/13.CHIP-CDEE.json
14,data/14.IMCS-V2-MRG.json
1.3,data/C_problem.json
1.4,data/D_problem.json
9,data/TCM-LitData.json
```

## 致谢


我们衷心感谢×××对本项目的巨大支持。🎉🎉🎉

同时，感谢参与本项目的全体成员！


