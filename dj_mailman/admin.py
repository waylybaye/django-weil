from django.contrib import admin
from dj_mailman.models import Mail


class MailAdmin(admin.ModelAdmin):
    list_display = ["to", "subject", "sender", "status"]

admin.site.register(Mail, MailAdmin)
