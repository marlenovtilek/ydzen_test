from rest_framework import routers
from . import views
from .models import Post, Comment

post_router = routers.DefaultRouter()
post_router.register(r'post', views.PostViewSet, basename=Post.__name__),
router = routers.DefaultRouter()
