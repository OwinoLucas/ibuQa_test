from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CreateUserAPIView, LoginApiView, CreateOrder, AllOrders

urlpatterns = [
    path('api/signup/', CreateUserAPIView.as_view()),
    path('api/login/', LoginApiView.as_view()),
    path('api/order/create/', CreateOrder.as_view(), name="create_order"),
    path('api/all-orders/', AllOrders.as_view(), name="all_orders"),
]