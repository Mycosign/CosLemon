from django.contrib import admin
from .models import Product, Payment, PremiumProduct, Blog
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

"""class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'subject', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'subject')
  list_per_page = 20

admin.site.register(Contactor, ContactAdmin)"""
admin.site.register(Product)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'amount', 'status', 'completed')
    list_filter = ('status', 'completed')
    actions = ['mark_as_complete']

    def mark_as_complete(self, request, queryset):
        queryset.update(status='COMPLETED', completed=True)
    mark_as_complete.short_description = "Mark selected payments as complete"

admin.site.register(Payment, PaymentAdmin)
#admin.site.register(Blog)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'user','subject', 'contact_date')
    list_filter = ('user', 'contact_date')
    search_fields = ('name', 'user__username', 'user__email')
    date_hierarchy = 'contact_date'
    ordering = ('-contact_date',)
    list_per_page = 20

    fieldsets = (
        ('Notification Details', {
            'fields': ('name', 'user', 'image','subject', 'message', 'contact_date')
        }),
    )

admin.site.register(Notification, NotificationAdmin)