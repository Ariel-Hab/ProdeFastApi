import hmac
import hashlib
import urllib.parse
import os
import requests

SSO_SECRET_KEY = os.environ.get("SSO_SECRET_KEY", "prode_sso_secret_12345")

def get_sso_url(user_id, user_name):
    payload = f"{user_id}:{user_name}".encode('utf-8')
    signature = hmac.new(
        SSO_SECRET_KEY.encode('utf-8'),
        payload,
        hashlib.sha256
    ).hexdigest()
    
    params = {
        "id": user_id,
        "name": user_name,
        "signature": signature
    }
    query_string = urllib.parse.urlencode(params)
    return f"http://localhost:8000/api/auth/external-login?{query_string}"

if __name__ == "__main__":
    url = get_sso_url("12345", "JuanPerez")
    print(f"Test SSO Login URL:\n{url}")
    print("\nAttempting to hit URL...")
    try:
        response = requests.get(url, allow_redirects=False)
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers}")
    except Exception as e:
        print(f"Error: {e}")
