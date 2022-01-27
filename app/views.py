from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest



# authorize razorpay client with API Keys.
client = razorpay.Client(auth=('rzp_test_xj4aUFvPEyWdSO', 'z7j1zVeq4EArVnGTkp8tjSy9'))
def homepage(request):
    order_amount = 50000
    order_currency = 'INR'
    payment_order = client.order.create(dict(amount=order_amount, currency=order_currency, payment_capture=1))
    payment_order_id = payment_order['id']
    context = {'amount':500, 'api_key': 'rzp_test_xj4aUFvPEyWdSO', 'order_id':payment_order_id}
    return render(request, 'main.html', context)