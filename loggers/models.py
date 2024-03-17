from django.db import models
from django.utils.translation import gettext_lazy as _
import utils

# Create your models here.


class RequestLog(models.Model):
    response_code = models.PositiveIntegerField(
        _('Response Code'),
    )
    method = models.CharField(
        _('API Method'),
        choices=utils.REQUEST_METHOD_CHOICES,
        max_length=10,
    )
    url = models.CharField(
        _('URL'),
        max_length=400,
    )
    request_received_at = models.DateTimeField(
        _('Request Received Time'),
        null=True,
        blank=True,
    )
    response_received_at = models.DateTimeField(
        _('Response Received Time'),
        null=True,
        blank=True,
    )
    utc_time_logged = models.DateTimeField(
        _('UTC Time Logged'),
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.method} {self.url} {self.utc_time_logged}'

    class Meta:
        db_table = 'request_logs'
        verbose_name = _('Request Log')
        verbose_name_plural = _('Request Logs')
        indexes = [
            models.Index(fields=['utc_time_logged', 'url']),
        ]






