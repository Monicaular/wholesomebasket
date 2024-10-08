from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    """
    Model representing a wishlist containing products that a user has saved.
    Each user can add a product to their wishlist only once.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user.username}'s wishlist"
