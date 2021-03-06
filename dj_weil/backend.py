from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
import requests
from dj_weil.models import Mail, MailStatus


class EmailBackend(BaseEmailBackend):
    def __init__(self, fail_silently=False, mailman_endpoint=None, token=None, **kwargs):
        super(EmailBackend, self).__init__(fail_silently, **kwargs)
        self.end_point = mailman_endpoint or settings.WEIL_END_POINT
        self.token = token or settings.WEIL_ACCESS_TOKEN

    def send_messages(self, email_messages):
        for email_message in email_messages:

            # save to database
            mail = Mail()
            mail.email = email_message
            mail.status = MailStatus.NORMAL
            mail.save()

            data = {
                'subject': email_message.subject,
                'to': email_message.to,
                'content': email_message.body,
                'sender': email_message.from_email,
                'token': self.token,
            }

            # Call weil api to send the email
            resp = requests.post(self.end_point, data)

            if resp.status_code == 200:
                mail.status = MailStatus.SUCCESS
            else:
                mail.status = MailStatus.FAILED

            # record the response messages from wei api
            mail.response = "STATUS: %s\nBODY: %s" % (resp.status_code, resp.content)
            mail.save()

            if mail.status == MailStatus.FAILED and not self.fail_silently:
                raise Exception(resp.content)
