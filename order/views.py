from django.shortcuts import render , redirect
from order.models import Order
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
import logging
# Create your views here.
logger = logging.getLogger("order.views")

def log_order_completion(order):
    logger.info(f"Order {order.pk} marked as completed by user at {timezone.now()}")

def mark_order_completed(request, order_id):
    order = Order.objects.get(pk=order_id)
    if not order.is_completed:
        order.is_completed = True
        order.save()
        # Message
        messages.success(request, \
            f"Order #{order.pk} marked as completed!")
        # Email (Optional)
        send_mail(
            "Your WonderShop Order is Complete!",
            f"Hi {order.customer_name}, your order \
            #{order.pk} has been marked as completed.",
            "your_email@wondershop.com",
            [order.email],)
        log_order_completion(order) # Add this call after completing the order
    else:
        messages.info(request, \
            f"Order #{order.pk} is already marked as completed.")
    # Redirect or return to detail view
    return redirect("your_desired_page")

    