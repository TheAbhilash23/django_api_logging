from rest_framework import routers

from loggers import views as loggers_views

router = routers.SimpleRouter()

router.register(
    r'loggers', loggers_views.RequestLogView,
    basename="loggers")
