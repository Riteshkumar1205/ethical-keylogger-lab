## 🔐 Ethical Keylogger – Secure Monitoring Tool (linux user)
**⚠️ Legal Disclaimer
This software is intended strictly for ethical, educational, and authorized cybersecurity research purposes.**

Unauthorized usage, including monitoring keystrokes, clipboard data, or screen content without the informed and verifiable consent of all users, is a violation of local, national, and international privacy and cybersecurity laws.

The user assumes full responsibility for any legal or ethical consequences resulting from the use of this software.

## 🧩 Project Overview
This tool is a consent-based, AES-encrypted, email-reporting keylogger designed for:

**Ethical hacking demonstrations**

**Cybersecurity education and workshops**

**Digital forensics research**

It supports real-time keystroke logging, screenshot capture, clipboard monitoring, and encrypted email reporting—with consent verification prior to activation.

## ✅ Key Features
**Feature	                Description**
Keystroke Logging	         Records all keyboard inputs along with active window titles and timestamps
Clipboard Monitoring       Monitors copy, cut, and paste activities on the system clipboard
Screenshot Capture	       Takes periodic screenshots; securely transmitted via email
AES Encryption	           Utilizes cryptography.Fernet to encrypt log data
Email Reporting	           Sends encrypted logs and screenshots via email with configurable settings
Consent Prompt	           Requires user approval before any monitoring begins
System Information	       Collects system metadata (username, IP addresses, timestamp)
Log Integrity Check	       Applies SHA256 hashing to verify log authenticity
Audit Logging	             Maintains local logs for traceability and compliance

## 🐧 Installation (Linux – Ubuntu / Debian / Kali)
~~~
sudo apt update && sudo apt install git python3 python3-pip python3-venv -y

git clone https://github.com/Riteshkumar1205/ethical-keylogger-lab.git
cd ethical-keylogger-lab

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# Optional (for screenshot support)
sudo apt install scrot python3-tk python3-dev -y
~~~

## 📦 Required Packages (Ensure These Are Installed)
To manually install essential Python dependencies within your virtual environment:
~~~
pip install pynput cryptography clipboard mss requests

To support active window tracking (if not already installed):

sudo apt install xdotool
~~~
## 🔐 Setting Environment Variables
Before executing the script, configure the necessary email variables in your terminal session:

~~~
export SENDER_EMAIL='your_email@gmail.com'
export EMAIL_PASSWORD='your_app_password'   # Use a secure App Password
export RECEIVER_EMAIL='receiver_email@gmail.com'
~~~
**Important: Do not hardcode sensitive credentials directly in the script. Always use environment variables**.

## 🚀 Running the Keylogger
To initiate the keylogger:
~~~
python keyloggers_2025.py
~~~
The script will prompt for explicit user consent.

Upon approval, it will begin capturing logs (keystrokes, clipboard data, screenshots).

Logs and captured images are encrypted and either saved locally or sent via email.

## ⚙️ Configuration & Customization
You may customize the script by modifying:

Screenshot intervals and formats

Logging frequency and batch size

Local log storage path

Email retry logic and triggers

Refer to the keyloggers_2025.py file for configuration parameters.

## 📄 License
**This project is licensed under the MIT License.**

You are free to use, modify, and distribute this software, provided that you include the original copyright
and licensing information. The software is provided “as is,” without any warranties.

## ⚖️ Legal & Ethical Use Policy
Consent Requirement
Consent must be explicit, informed, and verifiable.

Maintain proper documentation and store consent records securely.

Prohibited Use
Unauthorized monitoring of individuals or systems without consent is strictly forbidden.

Violations may lead to legal action under applicable cybercrime and privacy laws.

Intended Use Cases
Ethical hacking education

Penetration testing (with authorization)

Research and academic coursework

This tool is not intended for personal surveillance, corporate espionage, or any commercial deployment without explicit permission.

Legal Compliance
Users must comply with relevant laws and frameworks, including but not limited to:

India – Information Technology Act (Sections 66E, 72)

European Union – General Data Protection Regulation (GDPR)

United States – CFAA, ECPA

Other – National and regional privacy and data protection statutes

## 🛡️ Recommended Best Practices
Virtual Environments: Isolate dependencies for reproducibility and security

Data Encryption: Always encrypt logs and sensitive information

Secure Handling: Ensure safe transmission and storage of all monitored data

Audit Trails: Maintain comprehensive logs for accountability

Consent Documentation: Keep records of all consent approvals

Stay Informed: Regularly review relevant legal and ethical standards

## ⚠️ Final Disclaimer
This software is provided “as is,” without any warranties—express or implied.
The authors and contributors shall not be held liable for any misuse, damages, or legal consequences arising from its use.

By downloading or using this tool, you agree to:

Accept full legal responsibility for its deployment

Use it only in ethical and authorized contexts

**Abide by all local and international laws regarding digital privacy and monitoring**
