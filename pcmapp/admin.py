from django.contrib import admin
from .models import CustomUser,AddCash,Expense

admin.site.register(CustomUser)
admin.site.register(AddCash)
admin.site.register(Expense)

