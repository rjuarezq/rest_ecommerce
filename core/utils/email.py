from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv
from smtplib import SMTP, SMTP_SSL

from django.template.loader import get_template

SMTP_HOST = getenv("SMTP_HOST", "sandbox.smtp.mailtrap.io")
SMTP_PORT = getenv("SMTP_PORT", 2525)
SMTP_USERNAME = getenv("SMTP_USERNAME", "")
SMTP_PASSWORD = getenv("SMTP_PASSWORD", "")


@dataclass
class Email:
    to: str
    subject: str
    sender: str
    body: str = ""
    cc: str = ""
    bcc: str = ""

    def set_template_with_context(self, template: str, context: dict):
        self.body = get_template(template).render(context)

    def send(self):
        msg = self.create_email()
        self._send_message(msg)

    def create_email(self):
        email = MIMEMultipart()
        email["subject"] = self.subject
        email["from"] = self.sender
        email["to"] = self.to
        self.attach_html_body(email)
        return email

    def attach_html_body(self, email: MIMEMultipart):
        email.attach(MIMEText(self.body, "html"))

    def _send_message(self, msg: MIMEMultipart):
        # for test use SMTP for production use SMTP_SSL
        with SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
