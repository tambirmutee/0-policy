import requests
from zeropolicy.config import load_config

def get_csp_header(url):
    config = load_config()
    timeout = config.get("timeout", 5)
    user_agent = config.get("user_agent", "0-Policy/1.0")

    headers = {
        "User-Agent": user_agent
    }

    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        csp = response.headers.get("Content-Security-Policy")
        return csp
    except requests.exceptions.RequestException:
        return None
