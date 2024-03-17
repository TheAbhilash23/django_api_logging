from django.contrib import admin
from loggers import models


@admin.register(models.RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'response_code',
        'method',
        'url',
        'request_received_at',
        'response_received_at',
        'utc_time_logged',
    )

    readonly_fields = ('utc_time_logged',)
