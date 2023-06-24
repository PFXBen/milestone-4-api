import json
import os
import stripe
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from products.models import Product

# Create your views here.

@csrf_exempt  
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': os.getenv('STRIPE_PUBLISHABLE_KEY')}
        return JsonResponse(stripe_config, safe=False)
    
@csrf_exempt    
def create_checkout_session(request):
    if request.method == 'POST':
        domain_url = request.build_absolute_uri('/')[:-1]
        print(domain_url)
        try:

            #Info on purchases bought
            print(request.body)
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)     
            items = []
            for x in body:
                items.append(x)
            print(items)               


            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + '/orders/success/',
                cancel_url=domain_url + '/orders/cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=items,
                billing_address_collection='required',
                customer_creation='always',
                phone_number_collection={
                    'enabled':True
                },
                invoice_creation={
                    'enabled':True
                }
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = os.getenv("STRIPE_ENDPOINT_SECRET")
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'invoice.payment_succeeded':
        print(event)
        print(payment_intent)
        #stripe.PaymentIntent.get(event['data']['object']['id'])
        #payment_intent = event['data']['id']
        #product = Product.objects.get(stripe_id = product_bought)
        #Order.objects.create_order(1,product,event['id'],)
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)
        

class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'


