from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from .views import UserView

from django.contrib import admin
from django.urls import path
from product.views import ProductView
from django.conf.urls.static import static
from django.conf import settings

from order.views import OrderView, CartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/' , ProductView.as_view()),
    path('api/auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/orders/', OrderView.as_view()),
    path('api/cart/', CartView.as_view()),
    path('api/auth/users/' , UserView.as_view())
]

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
