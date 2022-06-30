
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Kinoapp.views import *

router = DefaultRouter()
router.register("aktyorlar", AktyorViewSet)
router.register("kinolar", KinoViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
