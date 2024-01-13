from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'message')
admin.site.register(Contact, ContactAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('name', 'number', 'question1', 'question2', 'question3', 'question4', 'question5','feedback')
admin.site.register(Feed, FeedbackAdmin)