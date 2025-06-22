## 🔐 Enhanced Ethical Keylogger – Secure Monitoring Tool
**⚠️ Legal Notice:**
This software is intended strictly for ethical, educational, and authorized research purposes. Unauthorized use—including monitoring someone’s keystrokes, clipboard data, or screen content without explicit, informed, and verifiable consent—violates local, national, and international privacy and cybersecurity laws. Misuse may result in civil lawsuits, criminal prosecution, fines, academic expulsion, or blacklisting. You, the user, are solely liable for any legal consequences arising from the misuse of this software.
Always obtain informed, written consent before monitoring any system.

## 🧩 Overview
This is a consent-based, encrypted, and email-reporting keylogger built for ethical hacking demonstrations, cybersecurity training, and forensic education. It supports real-time logging, screenshot capture, clipboard monitoring, and secure reporting via email—all while requiring explicit user consent before activation.

## ✅ Key Features
**Feature	Description**
Keystroke Logging	Captures all keyboard input with timestamps and active window context
Clipboard Monitoring	Logs clipboard activity (copy, cut, paste)
Screenshot Capture	Takes periodic screenshots, batch-processed and included in reports
AES Encryption	Encrypts logs using cryptography.Fernet
Email Reporting	Sends encrypted logs and images via email, with retry logic
Consent Verification	Requires explicit user consent before starting monitoring
System Information	Includes username, timestamp, public/private IP addresses
Log Integrity Hashing	SHA256 hash ensures log data has not been tampered with
Audit Logging	Maintains local audit logs for transparency

## 🛠 Installation
**Supported Platforms
Windows 10/11**

**Linux (Ubuntu, Debian, Kali)**

**macOS**

**Android (via Termux – limited functionality, CLI only)**

## 🪟 Windows
~~~
git clone https://github.com/Riteshkumar1205/ethical-keylogger-lab.git
cd ethical-keylogger-lab
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

Set environment variables for email (optional, but recommended):

set SENDER_EMAIL=your_email@example.com
set EMAIL_PASSWORD=your_app_password
set RECEIVER_EMAIL=receiver@example.com
~~~

## 🐧 Linux (Ubuntu/Debian/Kali)
~~~
sudo apt update && sudo apt install git python3 python3-pip python3-venv -y
git clone https://github.com/Riteshkumar1205/ethical-keylogger-lab.git
cd ethical-keylogger-lab
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

For screenshot support:

sudo apt install scrot python3-tk python3-dev -y
~~~

## 🍏 macOS
~~~
brew install git python
git clone https://github.com/Riteshkumar1205/ethical-keylogger-lab.git
cd ethical-keylogger-lab
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt


Permissions required:

Accessibility: System Preferences → Security & Privacy → Accessibility

Input Monitoring: System Preferences → Security & Privacy → Input Monitoring

Screen Recording: System Preferences → Security & Privacy → Screen Recording
~~~

## 🤖 Android (via Termux)
**Note: Full functionality is not supported due to sandboxing and security restrictions.**

~~~
pkg update && pkg upgrade
pkg install git python
git clone https://github.com/Riteshkumar1205/ethical-keylogger-lab.git
cd ethical-keylogger-lab
pip install -r requirements.txt
~~~
## ▶️ Usage
~~~
python enhanced_keylogger.py
~~~
Consent Verification: The program will prompt for explicit user consent before starting.

Monitoring: Logs keystrokes, clipboard activity, and takes screenshots at defined intervals.

Reporting: Encrypted logs and screenshots are sent via email or saved locally.

## 📄 License
**This project is licensed under the MIT License.
See the LICENSE file for full legal text.**

By using, modifying, or distributing this software, you agree to the terms of the MIT License, which permits free use, modification, and distribution of the software, provided the original copyright notice and license are included in all copies or substantial portions of the software. The software is provided "as is," without any warranty or liability from the authors or contributors.

## ⚖️ Legal and Ethical Use Policy
Explicit Consent Requirement
**Consent is Mandatory:**
This software must never be deployed or used without the explicit, informed, and verifiable consent of all monitored users. Consent should be documented and easily retrievable.

**No Unauthorized Monitoring:**
Monitoring another individual’s activity without their knowledge and consent is strictly prohibited and may constitute a violation of privacy laws.

Intended Use
**Educational and Research Purposes:**
This tool is designed for educational demonstrations, cybersecurity research, and authorized corporate monitoring. It is not intended for commercial deployment or unauthorized surveillance.

**Academic Integrity:**
Respect for intellectual property and privacy is fundamental. Unauthorized copying or use of this software—or any software—deprives creators of fair recognition and may harm the broader community.

**Legal Compliance**
Applicable Laws:
Users must ensure compliance with all local, national, and international laws relevant to privacy, data protection, and cybersecurity. Examples include:

Indian IT Act (Section 66E & 72)

General Data Protection Regulation (GDPR, EU)

Computer Fraud and Abuse Act (USA)

Personal Data Protection Bill (India, Draft)

Electronic Communications Privacy Act (USA)

Responsibility for Misuse:
The user is solely responsible for ensuring that their use of this software is lawful and ethical. The author and contributors accept no liability for any unauthorized or unlawful use of this software.

No Liability
Disclaimer of Liability:
The software is provided “as is,” without warranty of any kind, express or implied. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability arising from the use or misuse of the software.

User Responsibility:
By downloading, installing, or using this software, you acknowledge that you are solely responsible for any legal consequences resulting from your actions.

Responsible Deployment
Ownership and Permission:
Only deploy this software on systems you own or have explicit permission to monitor.

Transparency:
Maintain transparency with all monitored users regarding what data is collected, how it is used, and how it is protected.

## 🛡️ Best Practices
Isolate Dependencies:
Use a virtual environment to isolate project dependencies and avoid conflicts with system-wide Python installations.

Encrypt Sensitive Data:
Always encrypt log files and sensitive data to protect privacy and prevent unauthorized access.

Regular Audits:
Regularly review and audit logs to ensure compliance with ethical standards and legal requirements.

Consent Verification:
Never run the software without explicit consent from all monitored users. Maintain records of consent for accountability.

Secure Data Handling:
Follow data protection best practices, including secure storage, transmission, and deletion of sensitive information.

Stay Informed:
Keep abreast of changes in relevant laws and regulations to ensure ongoing compliance.


## ⚠️ Disclaimer
This software is provided “as is,” without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software
