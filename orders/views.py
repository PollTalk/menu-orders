# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, RequestContext, loader 
from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Item
from .forms import OrderTakingForm

def index(request):
	latest_items = Item.objects.order_by('-date_created')[:5]
	template = loader.get_template('orders/index.html')
	context = RequestContext(request, {
        'latest_items': latest_items,
        })
	return HttpResponse(template.render(context))

def create_orders(request):
	lunch_items = Item.objects.filter(category='LU')
	breakfast_items = Item.objects.filter(category='BF')
	snacks = Item.objects.filter(category='SN')
	if request.method == 'POST':
		pass
	variables = RequestContext(request,
	 {
	 'lunch_items': lunch_items,
	 'breakfast_items': breakfast_items,
	 'snacks': snacks
	 })
	return render_to_response(
        'orders/index.html',
        variables
        )

