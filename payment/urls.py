from django.urls import path
from .views import ProductPreview,CreatePaymentIntent, CreateCheckOutSession, stripe_webhook_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('webhook/', stripe_webhook_view, name='stripe-webhook'),
    path('product/<int:pk>/', ProductPreview.as_view(), name="product"),
    path('create-checkout-session/<pk>/', csrf_exempt(CreateCheckOutSession.as_view()), name='checkout_session'),
    path('create-payment-intent/', CreatePaymentIntent.as_view(), name='payment-intent')
    # path('payment-with-stripe/', CustomPaymentEndpoint.as_view())
    ]