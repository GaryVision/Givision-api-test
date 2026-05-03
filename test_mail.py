import os
import requests
import json

api_key = os.environ.get("AGENTMAIL_API_KEY")
# AgentMail 原生 API 的发信接口
url = "https://api.agentmail.to/v1/inboxes/givision@agentmail.to/messages"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "to": "2514047165@qq.com",
    "subject": "GitHub Actions Test",
    "text": "如果收到这封邮件，说明 API 调用成功！"
}

print("DEBUG: Sending request to AgentMail API...")
response = requests.post(url, headers=headers, json=data)

print(f"DEBUG: Status Code: {response.status_code}")
print(f"DEBUG: Response Body: {response.text}")

if response.status_code == 200 or response.status_code == 201:
    print("SUCCESS: 邮件已发送")
else:
    print("FAILURE: 发送失败")
