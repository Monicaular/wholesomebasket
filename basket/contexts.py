from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get("basket", {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal = quantity * product.price
        total += subtotal
        product_count += quantity
        basket_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "product": product,
                "subtotal": subtotal,
            }
        )

    if total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0

    grand_total = shipping + total

    context = {
        "basket_items": basket_items,
        "total": total,
        "product_count": product_count,
        "shipping": shipping,
        "free_shipping_delta": free_shipping_delta,
        "free_shipping_threshold": settings.FREE_SHIPPING_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
