from rest_framework import routers
from . import views
from .models import User

user_router = routers.DefaultRouter()
user_router.register(r'account', views.UserViewSet, basename=User.__name__),
router = routers.DefaultRouter()
