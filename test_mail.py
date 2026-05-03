import os
import requests
import json

# 从环境变量获取 API Key
api_key = os.environ.get("AGENTMAIL_API_KEY")

# 基础配置
base_url = "https://api.agentmail.to/v1"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def test_api():
    print("--- 步骤 1: 探测 API 根路径 ---")
    try:
        # 尝试访问根路径，查看服务器支持的路径结构
        root_res = requests.get(base_url, headers=headers)
        print(f"ROOT Status: {root_res.status_code}")
        print(f"ROOT Response: {root_res.text}")
    except Exception as e:
        print(f"Root Discovery Error: {e}")

    print("\n--- 步骤 2: 尝试发送测试邮件 ---")
    # 我们尝试最标准的路径结构
    # 如果上一步返回的 JSON 里显示有 'inboxes' 路径，我们需要根据返回的内容调整
    target_url = f"{base_url}/inboxes/givision@agentmail.to/messages"
    data = {
        "to": "2514047165@qq.com",
        "subject": "GitHub Actions Final Test",
        "text": "如果收到这封邮件，说明 API 路径已对齐。"
    }
    
    try:
        response = requests.post(target_url, headers=headers, json=json.dumps(data))
        print(f"Send Status: {response.status_code}")
        print(f"Send Response: {response.text}")
    except Exception as e:
        print(f"Send Error: {e}")

if __name__ == "__main__":
    test_api()
