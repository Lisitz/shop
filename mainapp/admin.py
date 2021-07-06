from django import forms

from django.forms import ModelChoiceField
from django.contrib import admin
g
from .models import *


class SneakersAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug = 'sneakers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AccessoriesAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug = 'accessories'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Sneakers, SneakersAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)