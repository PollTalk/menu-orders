from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from .models import Item, Order, Category, TakeOrder

def export_selected_objects(modeladmin, request, queryset):
	selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
	ct = ContentType.objects.get_for_model(queryset.model)
	return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))
export_selected_objects.short_description = "View the total cost of the selected orders"

class TakeOrderInline(admin.TabularInline):
 	model = TakeOrder
 	extra = 1

class ItemAdmin(admin.ModelAdmin):
	ordering = ('-date_created',)
	search_fields = ['item', 'price_per_item']
	list_display = ('item', 'price_per_item', 'category', 'date_created')
	list_filter = ['date_created', 'category']

class OrderAdmin(admin.ModelAdmin):
	actions = [export_selected_objects]
	inlines = (TakeOrderInline,)
	list_display = ('ordering_time', 'cost_of_order' )
	list_filter = ('ordering_time',)
	date_heirarchy = 'ordering_time'
	ordering = ('-ordering_time',)
	filter_horizontal = ('items',)

admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)


