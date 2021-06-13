from django.contrib import admin

# Register your models here.
from .models import User, Food, SpecialDiet
# Register your models here.
admin.site.register(User)
admin.site.register(Food)
admin.site.register(SpecialDiet)