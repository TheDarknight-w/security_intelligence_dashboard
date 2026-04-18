# api.py
import requests
import hashlib
from config import VT_API_KEY

def check_pwned(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            for line in res.text.splitlines():
                h, count = line.split(':')
                if h == suffix:
                    return f"Leaked ({count} times)"
            return "Safe (No leaks found)"
    except:
        return "Connection Error"
    return "Safe"

def check_url(url):
    headers = {"x-apikey": VT_API_KEY}
    try:
        # Submit URL
        res = requests.post("https://www.virustotal.com/api/v3/urls", headers=headers, data={"url": url})
        if res.status_code != 200: return "API Error"
        
        # Get Analysis result
        analysis_id = res.json()["data"]["id"]
        result = requests.get(f"https://www.virustotal.com/api/v3/analyses/{analysis_id}", headers=headers)
        if result.status_code == 200:
            stats = result.json()["data"]["attributes"]["stats"]
            return f"Malicious: {stats['malicious']} | Harmless: {stats['harmless']}"
    except:
        return "Request Failed"
    return "Analysis Pending"