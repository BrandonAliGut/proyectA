from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', UserViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginApiView.as_view()),
    path('userbaic', ExampleView.as_view()),
]