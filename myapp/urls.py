#define URL route for index() view
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

router=DefaultRouter()
router.register(r'tables',views.BookingViewSet)
urlpatterns = [
    path('menu/',views.MenuItemsView.as_view()),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view()),
    path('restaurant/booking/',include(router.urls))
]
