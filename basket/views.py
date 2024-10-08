from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from products.models import Product
from decimal import Decimal


def view_basket(request):
    """A view that renders the basket content page"""

    return render(request, "basket/basket.html")


def add_to_basket(request, item_id):
    """Add or update the quantity of a product in the shopping basket."""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity", 1))
    redirect_url = request.POST.get("redirect_url", "products")
    basket = request.session.get("basket", {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request,
            f"Updated {product.name} quantity to {int(basket[item_id])}",
            extra_tags="show_basket_preview",
        )
    else:
        basket[item_id] = quantity

    request.session["basket"] = basket
    messages.success(
        request,
        f"You added {quantity} x {product.name} to your basket",
        extra_tags="show_basket_preview",
    )

    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    basket = request.session.get("basket", {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
            request,
            f"Updated {product.name} quantity to {int(basket[item_id])}",
            extra_tags="show_basket_preview",
        )
    else:
        basket.pop(item_id, None)
        messages.success(
            request,
            "Item removed from your basket",
            extra_tags="show_basket_preview",
        )

    request.session["basket"] = basket
    return redirect(reverse("view_basket"))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        basket = request.session.get("basket", {})

        if str(item_id) in basket:
            del basket[str(item_id)]
            request.session["basket"] = basket
            messages.success(
                request,
                "Item successfully removed from basket.",
                extra_tags="show_basket_preview",
            )
            return HttpResponse(status=200)
        else:
            messages.error(request, "Item not found in basket.")
            return HttpResponse(status=404)

    except Exception as e:
        messages.error(request, f"Error removing item from basket: {str(e)}")
        return HttpResponse(status=500)
