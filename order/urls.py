from order import views
from django.urls import path

urlpatterns = [
    path('mail/<order_id>', views.mark_order_completed , name='completed'),
]