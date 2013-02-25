import base64
from datetime import datetime
import pickle
from django.db import models


class MailStatus:
    NORMAL = 1
    FAILED = 2
    SUCCESS = 3


MAIL_STATUS_CHOICES = (
    (MailStatus.NORMAL, "Processing"),
    (MailStatus.FAILED, "Failed"),
    (MailStatus.SUCCESS, "Success")
)


class Mail(models.Model):
    to = models.CharField(max_length=200)
    sender = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)

    data = models.TextField()
    status = models.SmallIntegerField(choices=MAIL_STATUS_CHOICES)

    response = models.TextField(null=True)

    created_at = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.subject

    def _set_email(self, email_message):
        self.data = base64.encodestring(pickle.dumps(email_message))
        self.to = ",".join(email_message.to)[:200]
        self.sender = email_message.from_email[:200]
        self.subject = email_message.subject[:200]

    def _get_email(self):
        return pickle.loads(base64.decodestring(self.data))

    email = property(_get_email, _set_email, doc="")
