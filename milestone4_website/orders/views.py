import json
import os
import stripe
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from users.models import User
from orders.models import Order
from products.models import Product

# Create your views here.
@csrf_exempt  
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': os.getenv('STRIPE_PUBLISHABLE_KEY')}
        return JsonResponse(stripe_config, safe=False)
    
@csrf_exempt    
@login_required
def create_checkout_session(request):
    if request.method == 'POST':
        current_user = request.user
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
            customer_id = None
            customer_address = None
            customer_details = None
            customer_creation='always'
            full_name = current_user.first_name + ' ' + current_user.last_name
            if current_user.stripe_customer_id is not None:
                customer_address = {}
                customer_details = {}
                customer_creation = None
                customer_id = current_user.stripe_customer_id
                customer_address['line1'] = current_user.address_1
                customer_address['line2'] = current_user.address_2
                customer_address['city'] = current_user.address_city
                customer_address['country'] = current_user.address_country
                customer_address['postal'] = current_user.address_postal
                customer_details['address'] = customer_address,
                customer_details['email'] = current_user.email
                customer_details['name'] = full_name

            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + '/orders/success/',
                cancel_url=domain_url + '/orders/cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=items,
                billing_address_collection='required',
                customer_email=current_user.email,
                customer_creation=customer_creation,
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
        invoice_id = event['data']['object']['id']
        user_email = event['data']['object']['customer_email']
        user_stripe_id = event['data']['object']['customer']
        user_address = event['data']['object']['customer_address']
        user_phone = event['data']['object']['customer_phone']
 
        this_user = User.objects.get(email=user_email)

        this_user.stripe_customer_id=user_stripe_id
        this_user.address_1=user_address['line1']
        this_user.address_2=user_address['line2']
        this_user.address_city=user_address['city']
        this_user.address_country=user_address['country']
        this_user.address_postal=user_address['postal_code']
        this_user.phone = user_phone
        this_user.save()
        
        # for each product in the invoice, create an order record...
        products_in_invoice = event['data']['object']['lines']['data'] #array of products in invoice
        for x in products_in_invoice:
            print(x)
            lineitem_product_id = x['price']['product']
            quantity = x['quantity']
            # Update local quantity of product left
            product_from_db = Product.objects.get(stripe_id=lineitem_product_id)
            product_from_db.quantity = product_from_db.quantity - quantity
            product_from_db.save()
            # Create copy of order in our db
            Order.objects.create_order(this_user,product_from_db, stripe_invoice_id=invoice_id,quantity=quantity)
            

        print("Payment was successful.")

    return HttpResponse(status=200)
        

class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'


