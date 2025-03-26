import random
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from pyexpat.errors import messages

from users.models import Customer


@receiver(post_save, sender=User)
def create_vat_number(sender, instance, created, **kwargs):
    if created and instance.VAT_Number:
        instance.VAT_Number = str(random.randint(100000000, 100000000))
        instance.save()

        superusers = User.objects.filter(is_superuser=True)
        recipient_list = [user.email for user in superusers if user.email]

        if recipient_list:
            subject = "Change in customer information!"
            message = f"Customer {instance.name} data has been updated or created."
            send_mail(subject, message, "olmosnormuminov02@gmail.com", recipient_list)

