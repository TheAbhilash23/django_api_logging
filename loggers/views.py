from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from loggers import models
from loggers import serializers
from rest_framework import status
from rest_framework.response import Response

import threading

api_lock = threading.Lock()

__batch__ = []


class RequestLogView(ModelViewSet):
    queryset = models.RequestLog.objects.all()
    serializer_class = serializers.RequestLogSerializer

    @action(methods=['POST'],
            detail=False, url_path='create_trusted_log',
            permission_classes=(),
            )
    def create_trusted_log(self, request, *args, **kwargs):
        with api_lock:
            request = models.RequestLog(
                response_code=request.data.get('response_code'),
                method=request.data.get('method'),
                url=request.data.get('url'),
                request_received_at=request.data.get('request_received_at'),
                response_received_at=request.data.get('response_received_at'),
            )

            if len(__batch__) < 500:
                __batch__.append(request)
                response = {'message': 'Response Recorded in __batch__'}
                return Response(response, status=status.HTTP_201_CREATED,)
            else:
                models.RequestLog.objects.bulk_create(__batch__)
                print('len __batch__ 500', len(__batch__))
                __batch__.clear()
                response = {'message': 'Bus Transported to database'}
                return Response(response, status=status.HTTP_201_CREATED,)

