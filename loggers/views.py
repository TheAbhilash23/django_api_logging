from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from loggers import models
from loggers import serializers


class RequestLogView(ModelViewSet):
    queryset = models.RequestLog.objects.all()
    serializer_class = serializers.RequestLogSerializer

    @action(methods=['POST'],
            detail=False, url_path='create_trusted_log',
            permission_classes=(),
            )
    def create_trusted_log(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


