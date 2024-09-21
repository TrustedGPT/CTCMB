# 下载文件

（1）Zip格式

```python
git clone “https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks.git”&& cd TCM-Assessment-Benchmarks/data
```

（2）[百度云链接](通过网盘分享的文件：TCM-Assessment-Benchmarks
链接: https://pan.baidu.com/s/1upBEw9YXnYnXuJ21W7uyKQ?pwd=g2a8 提取码: g2a8 
--来自百度网盘超级会员v6的分享)

[Leaderboard](https://cmedbenchmark.llmzoo.com/static/leaderboard.html)

# 结构（Structure）

数据集包含5个主要类别和13个子类别。每个子类别有100~200道题目。

目录及具体的数量

| 一级目录     | 二级目录                                                 | 数量 |
| ------------ | -------------------------------------------------------- | ---- |
| 中医知识问答 | TCM-ED                                                   | 720  |
|              | TCM-DID                                                  | 100  |
|              | TCM-FT                                                   | 100  |
| 医学语言生成 | 根据输入的临床症状，写出相关的口语化问句                 | 200  |
|              | 根据原有对话、新增对话、原有病历内容，对原有病历进行修改 | 199  |
|              | TCM-CHGD                                                 | 100  |
|              | TCMeEE                                                   | 100  |
| 中医推理     | TCM-SRT                                                  | 100  |
|              | 根据患者的症状描述输出的病症概率并且解释                 | 189  |
| 中医语言理解 | TCM-LitData                                              | 100  |
| 中医诊断     | Med-Treat                                                | 100  |
|              | TCM-Clin                                                 | 100  |
|              | TCM-DS                                                   | 200  |

# 数据集描述

点击超链接可以查看到不同数据集格式要求

## 中医知识问答

TCM-ED（Traditional Chinese Medicine Examination Dataset，TCM-ED）旨在测试模型对中医基础知识的掌握及推理能力。该数据集包含[A型题（最佳选择题）](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/data_format/A_problem.json)、[B型题（病历摘要型最佳选择题）](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/data_format/B_problem.json)、[C型题（共用题干选择题）](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/data_format/C_problem.json)以及[D型题（共用选项选择题）](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/data_format/D_problem.json)。其中，A、C、D型题的数据来源于中医职业医师考核和中医主治医师考核的真题；而B型题则是利用GPT-4模型，结合[《中医临床诊疗术语—第2部分：证候》](https://www.cacm.org.cn/wp-content/uploads/2022/03/%E4%B8%AD%E5%8C%BB%E4%B8%B4%E5%BA%8A%E8%AF%8A%E7%96%97%E6%9C%AF%E8%AF%AD-%E7%AC%AC2%E9%83%A8%E5%88%86%EF%BC%9A%E8%AF%81%E5%80%99.pdf)的知识生成的。

[中医判断说明数据集，（Traditional Chinese Medicine Diagnostic Indication Dataset，TCM-DID）](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/data_format/3.TCM-DID Dataset.json)旨在评估模型对中医基础理论的掌握程度及其推理能力。该数据集涵盖中医的核心哲学，涵盖了藏象理论、精气血津液神的调和、经络运行、体质辨识、病因与病机分析，以及养生和疾病预防的原则。其特点在于采用“先判断后解释”的题目设计，要求模型不仅要判断陈述的正确性，还需阐明判断依据。

[中医基础理论数据集（Traditional Chinese Medicine Fundamental Theory Dataset，TCM-FT）](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/data_format/4.TCM-FT.json) 旨在评估模型对中医基础理论的掌握能力，内容覆盖诊断方法、

疾病与证候、中药与方剂、针灸推拿等领域。数据集包括内经、伤寒论、金匮要略、温病学、中医基础理论、中医诊断学、中药学、方剂学、内科学、外科学、妇科学、儿科学、针灸学、中医各家学说等领域的知识。通过传统问答题形式，全面评估模型对中医理论的理解和掌握程度。

## **医学语言生成**

[病例生成数据集（Traditional Chinese Medicine Case History Generation Dataset，TCM-GHGD）](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/data_format/5.TCM-CHGD.json)，该数据集用于评估模型将中医问诊的医患对话转化为标准格式病例的能力。内容包括主诉、现病史、辅助检查、既往史、诊断和建议等关键要素。

[中医实体抽取数据集（Traditional Chinese Medicine Entity Extraction Dataset，TCMeEE）](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/data_format/8.TCMeEE.json)是面向中医学文本的命名实体识别数据集。这个数据集的主要目的是评估和测试模型从真实的医学文书中提取特定实体信息的能力。具体来说，对于给定的一组纯医学文本，任务的目标是识别并抽取出与中医相关的实体。

## **中医推理**

[中医语义推理数据集（Traditional Chinese Medicine Semantic Reasoning Task,TCM-SRT）](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/data_format/10.TCM-SRT.json)题干由三个主要部分构成：前提（premise）、假设（hypothesis）和选项（options），最终要求模型判断假设与前提之间的逻辑关系。

## **中医语言理解**

[中医文献数据集（Traditional Chinese Medicine Literature Data，TCM-LitData）](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/data_format/9.TCM-LitData.json)旨在评估模型在中医专业知识理解、信息提取、逻辑推理及知识应用等方面的能力。每条数据包括文献文本以及由人工标注产生的若干对（问题，答案）。其中问题均由人工标注产生，答案是段落中的文本中的连续片段。

## **中医诊断**

[中医症候数据集（Traditional Chinese Medicine Disease-Symptom Dataset,TCM-DS）](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/data_format/2.TCM-DS Dataset.json)旨在通过多项选择题的形式，评估模型对中医疾病与症状的辨析能力。该数据集覆盖了多种中医病症及其典型症状表现。

[医学治疗（Medical Treatment，Med-Treat）](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/data_format/6.Med-Treat.json)要求通过分析患者症状，给出合理的中医治疗方案。模型需要对这些信息进行深入、全面、系统的分析，给出方剂名称、组成和服用方法。

[中医诊断数据集（Traditional Chinese Medicine Clinical Dataset）](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/data_format/7.TCM-Clin.json)致力于评估模型在模拟真实临床情境下的知识运用能力，验证其能否有效利用中医理论应对复杂医疗挑战，提供切实可行的辅助诊断支持。该数据集要求模型精确提炼患者通过传统四诊（望、闻、问、切）获得的信息，包括直观的身体状况与系统性检查结果，进而综合分析并提出精准的中医诊断结论。

# 如何提交和评估

## **环境配置**

确保你的开发环境已经安装了[文件](https://github.com/Wayyuanyuan/TCM-Assessment-Benchmarks/blob/main/requirements.txt)要求的Python库

##  配置 API 密钥和 URL

> [!NOTE]
>
> 在这里，只提供`openai`、`Spart`、`ERNIE`调用方式的配置模版，如果调用模型有其他需求，请按照样例修改。

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

#### 不同的大模型有不同的 SDK 和 API 接口。你需要根据具体的模型提供商提供的文档来调整你的代码。

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
​        {
​            "role": "user",
​            "content": role_prompt+msg
​        }
​        ])
​    if response["body"]:
​        return response["body"]["result"]
​    else:
​        raise ValueError("Empty response from API")
```

## 运行项目

```
#example_input.csv 保存了所有数据集的路径
python run.py -i example_input.csv -m model_name
```

> [!IMPORTANT]
>
> `example_intpu.csv`文件格式要求：
>
> `question_id`代表处理不同数据使用的不同评估方法，`file`代表着传入的数据，这些[数据格式](#数据集描述)必须满足超链接中的要求。

完整的`example_input.csv`如下

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
