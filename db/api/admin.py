from django.contrib import admin
from . models import LoginInfo
from . models import Member
from . models import PurchaseRequest
from . models import Invoice
from . models import Item

# Register your models here.
admin.site.register(Member)
admin.site.register(LoginInfo)
admin.site.register(PurchaseRequest)
admin.site.register(Invoice)
admin.site.register(Item)