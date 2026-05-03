import os
import requests

api_key = os.environ.get("AGENTMAIL_API_KEY")

# 1. 必须先定义 Headers (确保 x-api-key 或 Authorization 放在这里)
headers = {
    "x-api-key": api_key,  # 有些文档要求 x-api-key
    "Authorization": f"Bearer {api_key}", # 有些要求 Bearer
    "Content-Type": "application/json"
}

# 2. 第一步：侦测有效的 Inbox 列表（这是为了确认 API 是否连通）
list_url = "https://api.agentmail.to/v1/inboxes"
print("DEBUG: Fetching Inbox list...")
try:
    response_list = requests.get(list_url, headers=headers)
    print(f"DEBUG: List Status: {response_list.status_code}")
    print(f"DEBUG: List Response: {response_list.text}")
except Exception as e:
    print(f"DEBUG: List Request Error: {e}")

# 3. 第二步：发送邮件
# 注意：大部分 API 发信路径是 /v1/messages，而不是 /v1/inboxes
send_url = "https://api.agentmail.to/v1/messages" 
data = {
    "from": "givision@agentmail.to",
    "to": "2514047165@qq.com",
    "subject": "GitHub Actions Test",
    "text": "如果收到这封邮件，说明 API 调用成功！"
}

print("DEBUG: Sending request to AgentMail API...")
try:
    response_post = requests.post(send_url, headers=headers, json=data)
    print(f"DEBUG: Post Status Code: {response_post.status_code}")
    print(f"DEBUG: Post Response Body: {response_post.text}")
except Exception as e:
    print(f"DEBUG: Post Request Error: {e}")
