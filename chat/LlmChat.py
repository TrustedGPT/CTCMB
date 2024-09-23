import json
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models
class LlmChat:

    history = []

    def __init__(self,
                 model: str = ""):
        self.model = model
        self.client = [hunyuan_client.HunyuanClient(
            credential.Credential("AKID120tswvmU6ZyISREsLgrreeR2SffS4Tf", "5ylOtFR0Vt686xcEmDUfihaM9rNn6MUU"),region="ap-guangzhou")]

    def chat(self, msg: str,
             role_prompt: str = "你是一个专业中医医生，能够准确全面的解答中医问题。本次对话，均只采用中文提问和回答。"):
        try:
            req = models.ChatCompletionsRequest()
            messages = {
                "Messages": [{"Role": "system", "Content": role_prompt}, {"Role": "user", "Content": msg}],
                "Model": self.model,
            }
            req.from_json_string(json.dumps(messages))
            resp = self.client[0].ChatCompletions(req)
            if resp and resp.Choices and resp.Choices[0].Message.Content:
                return resp.Choices[0].Message.Content
            else:
                print(f"错误：没有收到有效的响应，消息: {msg}")
                return None
        except TencentCloudSDKException as err:
            print(err)
