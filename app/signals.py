from django.core.mail import send_mail
from django.db.models.signals import post_save

from users.models import Customer


def create_category(sender, instance, created, **kwargs):
    if created:
        print("Category created")
        send_mail(
            f"Hello Dear!",
            f'Category {instance.title} successfully inserted',
            'olmosnormuminov02@gmail.com',
            [user.email for user in Customer.objects.filter(is_superuser=True)],

        )

post_save.connect(create_category, sender=Customer)
