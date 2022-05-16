from django.contrib import admin
from django.urls import path, include
from app.views import messageModelViewSet, UserModelViewSet, CustomAuthToken
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token   ## 1. To generate token using end point with username and password
from app.views import CustomAuthToken                          ## 2. To generate token using end point with username and password with additional info
from app.models import create_auth_token                       ## 3. Signal direct generate on register


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('mess', messageModelViewSet,basename="mess")
router.register('user', UserModelViewSet,basename="user")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', obtain_auth_token),              ## 1. To generate token using end point with username and password (function)
    path('gettokenc/', CustomAuthToken.as_view()),     ## 2. To generate token using end point with username and password with additional info
    path('gettokens/', create_auth_token)              ## 3. Signal direct generate on register 
]
