from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from loggers import models


class RequestLogSerializer(ModelSerializer):

    class Meta:
        model = models.RequestLog
        fields = (
            'id',
            'response_code',
            'method',
            'url',
            'request_received_at',
            'response_received_at',
            'utc_time_logged',
            
        )


