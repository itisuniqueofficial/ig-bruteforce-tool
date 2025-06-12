
# Insta Password Tester

⚠️ **Disclaimer:**  
This tool is for educational and security testing purposes only. Do not use it on any Instagram accounts that you do not own or have explicit permission to test. Unauthorized access to online accounts is illegal and unethical.

## About

Insta Password Tester is a simple tool to perform login testing on Instagram using a wordlist of passwords. It uses Instagram's mobile API endpoints to attempt authentication.

## Features

- Login attempts using Instagram's private API.
- Supports custom wordlists.
- Handles bad passwords, challenges (2FA), and unknown responses.
- Random device ID for each request.
- Rate limiting delays to help reduce the chance of temporary bans.

## Requirements

- Python 3.x
- `requests` module

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/insta-password-tester
cd insta-password-tester
pip install -r requirements.txt
````

## Usage

Run the script:

```bash
python instagram_brute_force.py
```

* Enter the Instagram username you want to test.
* Provide the full path to your password wordlist file (e.g. `wordlist.txt`).

Example:

```bash
[+] Enter Username: target_username
[+] Enter Password List File Path (e.g., wordlist.txt): wordlist.txt
```

## Important Notes

* Instagram has strict security measures such as rate limiting, IP bans, and 2FA.
* Use VPN or proxies at your own risk to avoid detection.
* This tool is for demonstration purposes and may not work effectively on protected accounts.

## Legal Disclaimer

This tool is for educational purposes only. The creator is not responsible for any misuse, abuse, or illegal activities performed with this software.
