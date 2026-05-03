import os
import sys
from agentmail import AgentMail

# 1. 强制打印环境变量状态
key = os.environ.get("AGENTMAIL_API_KEY")
print(f"DEBUG: API Key exists: {key is not None}")
if key:
    print(f"DEBUG: API Key length: {len(key)}")

# 2. 尝试执行发信
try:
    print("DEBUG: Initializing AgentMail Client...")
    client = AgentMail(api_key=key)
    print("DEBUG: Client initialized.")
    
    print("DEBUG: Attempting to send email...")
    response = client.inboxes.send(
        inbox_id="givision@agentmail.to",
        to="2514047165@qq.com",
        subject="GitHub Actions Test",
        text="If you see this, the API works."
    )
    print(f"DEBUG: Send response: {response}")
except Exception as e:
    print(f"DEBUG: Exception occurred: {e}")
    sys.exit(1)