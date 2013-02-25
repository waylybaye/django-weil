from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
import requests


class EmailBackend(BaseEmailBackend):
    def __init__(self, fail_silently=False, mailman_endpoint=None, token=None, **kwargs):
        super(EmailBackend, self).__init__(fail_silently, **kwargs)
        self.end_point = mailman_endpoint or settings.MAILMAN_END_POINT
        self.token = token or settings.MAILMAN_ACCESS_TOKEN

    def send_messages(self, email_messages):
        for email_message in email_messages:
            data = {
                'subject': email_message.subject,
                'to': email_message.to,
                'content': email_message.body,
                'sender': email_message.from_email,
                'token': self.token,
            }
            resp = requests.post(self.end_point, data)
            print "REQUEST:"
            print data
            print "RESPONSE:"
            print resp.status_code, resp.content
