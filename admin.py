from django.contrib import admin
from .models import Supplier, Drug, Sale, SaleItem

admin.site.register(Supplier)
admin.site.register(Drug)
admin.site.register(Sale)
admin.site.register(SaleItem)
