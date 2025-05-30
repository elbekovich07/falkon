import random
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.text import slugify

from .managers import CustomUserManager


class Customer(AbstractBaseUser):
    username = None
    name = models.CharField(max_length=100, unique=True,null=False, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    VAT_Number = models.CharField(max_length=9, unique=True, blank=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.slug or self.slug.strip() == "":
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Customer.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        if not self.VAT_Number:
            self.VAT_Number = str(random.randint(100000000, 999999999))

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.email} {self.VAT_Number}"
