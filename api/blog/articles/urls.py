from django.urls import re_path, include
from rest_framework import routers

from .views import ListTodo


router = routers.SimpleRouter()
router.register(r'articles', ListTodo)

urlpatterns = [
    re_path('', include(router.urls))
]