import os
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product=cart_item.product
                            name=cart_item.product.name
                            price=cart_item.product.sell_price()
                            quantity=cart_item.quantity


                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                       В наличии - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()
                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()
                        messages.success(request, 'Заказ оформлен!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('cart:order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            }
        form = CreateOrderForm(initial=initial)
    context = {
        'title': 'Home - Оформление заказа',
        'form': form,
        'orders': True,
    }
    return render(request, 'orders/create_order.html', context=context)

# def get_link(request):
#     phone = '79110921262'
#     email = 'ludmila.butakova@gmail.com'
#     price = '280000'
#     service = 'Абонемент на пробное групповое занятие'
#     style = 'Групповые занятия'

#     url = 'https://securepay.tinkoff.ru/v2/Init'
#     headers = {'Content-type': 'application/json',
#                'Accept': 'text',
#                'Accept-Encoding': 'utf-8'}
#     data = {
#         "TerminalKey": "1699899924888DEMO",
#         "Amount": price,
#         "OrderId": "6",
#         "Description": service + " (Направление: " + style + " )",
#         "Token": "kgcuyp0pg47y78px",
#         "DATA": {
#             "Phone": phone,
#             "Email": email
#         },
#         "Receipt": {
#             "Email": email,
#             "Phone": phone,
#             "Taxation": "osn",
#             "Items": [
#                 {
#                     "Name": service + " (Направление: " + style + " )",
#                     "Price": price,
#                     "Quantity": 1,
#                     "Amount": price,
#                     "Tax": "vat10",
#                     "Ean13": "303130323930303030630333435"
#                 },
#             ]
#         }
#     }
#     session = requests.Session()
#     session.verify = False
#     session.trust_env = False
#     os.environ['CURL_CA_BUNDLE'] = ""
#     requests.urllib3.disable_warnings()
#     response = session.post(url, data=json.dumps(data), headers=headers).json()
#     answer = response.get("PaymentURL")
#     field_link.delete(0, 255)
#     field_link.insert(0, str(answer))