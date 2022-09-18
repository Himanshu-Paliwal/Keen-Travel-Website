from django.contrib import admin
from .models import Vacation

from .models import Customer
# Register your models here.

admin.site.register(Customer)
admin.site.register(Vacation)