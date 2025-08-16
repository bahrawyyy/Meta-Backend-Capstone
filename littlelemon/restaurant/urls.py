from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)  # 'tables/' URL will map to BookingViewSet

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
]