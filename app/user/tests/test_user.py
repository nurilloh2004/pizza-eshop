"""
Tests for the user API.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)