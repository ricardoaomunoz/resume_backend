from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = "main"

urlpatterns = [
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify')
]   


# urlpatterns = [
#     # path('', views.IndexView.as_view(), name="home"),
#     # path('', views.as_view(), name=""),
#     # path('', views.as_view(), name=""),
#     # path('', views.as_view(), name=""),
#     # path('', views.as_view(), name=""),
#     # path('', views.as_view(), name=""),    
# ]