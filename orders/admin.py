from django.contrib import admin
from .models import Item, Order

class ItemAdmin(admin.ModelAdmin):
	ordering = ('-date_created',)
	search_fields = ['item', 'price_per_item']
	list_display = ('item', 'price_per_item', 'category', 'date_created')
	list_filter = ['date_created', 'category']

class OrderAdmin(admin.ModelAdmin):
	list_display = ('ordering_time', 'cost_of_order')
	list_filter = ('ordering_time',)
	date_heirarchy = 'ordering_time'
	ordering = ('-ordering_time',)
	filter_horizontal = ('items',)

admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)