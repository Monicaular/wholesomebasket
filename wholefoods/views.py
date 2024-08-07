import requests
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseServerError


def custom_404_page(request, exception):
    """
    Custom handler for 404 (Page Not Found) errors.
    """
    return render(request, "404.html", status=404)


def custom_500_page(request):
    """
    Custom handler for 500 (Internal Server Error) errors.
    """
    return render(request, "500.html", status=500)


def about_us(request):
    return render(request, "about_us.html")


def privacy_policy(request):
    return render(request, "privacy-policy.html")
