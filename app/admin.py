from django.contrib import admin

from app.models import *
from users.models import CustomUser

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Images)
admin.site.register(CustomUser)
