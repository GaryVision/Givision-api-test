import os
import requests

api_key = os.environ.get("AGENTMAIL_API_KEY")

# AgentMail 标准 API 调用逻辑
# 尝试使用最新的标准路径
base_url = "https://api.agentmail.to/v1"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 1. 探测路由
print("DEBUG: Testing connection to API...")
try:
    # 尝试访问所有 Inboxes
    res = requests.get(f"{base_url}/inboxes", headers=headers)
    print(f"DEBUG: Inbox List Status: {res.status_code}")
    print(f"DEBUG: Inbox List Response: {res.text}")
    
    # 2. 发送邮件（如果在上一步返回了 200，说明 API 通了）
    if res.status_code == 200:
        data = {
            "to": "2514047165@qq.com",
            "subject": "GitHub Actions Test",
            "text": "API 通信成功！"
        }
        # 很多 API 需要把 inbox_id 放在路径里或作为参数
        # 这里尝试标准的发送路径
        send_res = requests.post(f"{base_url}/messages", headers=headers, json=data)
        print(f"DEBUG: Send Status: {send_res.status_code}")
        print(f"DEBUG: Send Response: {send_res.text}")
        
except Exception as e:
    print(f"DEBUG: Error: {e}")
