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

bus = []


class RequestLogView(ModelViewSet):
    queryset = models.RequestLog.objects.all()
    serializer_class = serializers.RequestLogSerializer

    @action(methods=['POST'],
            detail=False, url_path='create_trusted_log',
            permission_classes=(),
            )
    def create_trusted_log(self, request, *args, **kwargs):
        with api_lock:
            passenger = models.RequestLog(
                response_code=request.data.get('response_code'),
                method=request.data.get('method'),
                url=request.data.get('url'),
                request_received_at=request.data.get('request_received_at'),
                response_received_at=request.data.get('response_received_at'),
            )

            if len(bus) < 500:
                bus.append(passenger)
                response = {'message': 'Response Recorded in bus'}
                return Response(response, status=status.HTTP_201_CREATED,)
            else:
                models.RequestLog.objects.bulk_create(bus)
                print('len bus 500', len(bus))
                bus.clear()
                response = {'message': 'Bus Transported to database'}
                return Response(response, status=status.HTTP_201_CREATED,)

