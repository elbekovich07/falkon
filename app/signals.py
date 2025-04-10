from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from users.models import Customer

def create_category(sender, instance, created, **kwargs):
    if created:
        print("Category created")
        superusers = User.objects.filter(is_superuser=True)
        recipient_list = [user.email for user in superusers if user.email]

        send_mail(
            "Hello Dear!",
            f'Customer {instance.name} successfully inserted',
            'olmosnormuminov02@gmail.com',
            recipient_list,
        )

post_save.connect(create_category, sender=Customer)
