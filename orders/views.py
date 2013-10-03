# Create your views here.
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, RequestContext, loader 
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
from .models import Item, CategorizeItem, Order, TakeOrder


def index(request):
	latest_items = Item.objects.order_by('-date_created')[:5]
	template = loader.get_template('orders/index.html')
	context = RequestContext(request, {
        'latest_items': latest_items,
        })
	return HttpResponse(template.render(context))

def create_orders(request):
	categories = CategorizeItem.objects.all()
	errors = []
	success = ''
	reciept = None
 	if request.method == 'POST':
 		if not request.POST.get('items', ''):
 			errors.append('No item was selected')
 		if not errors:
 			order_saved = _handle_submitted_data(request)
 			if order_saved:
 				messages.info(request, 'The order was successfully sent')
 			return HttpResponseRedirect('/')
 	else:
 		pass
 	variables = RequestContext(request,
 	 {
 	 	'categories': categories,
 	 	'errors': errors,
 	 	'messages': messages,
 	 })
 	return render_to_response(
         'orders/index.html',
         variables
         )

def _handle_submitted_data(request):
	order_items = []
	cost_of_order = 0
	items = request.POST.getlist('items')
	for pk in items:
		item = get_object_or_404(Item, pk=pk)
		price = item.price_per_item
		if item and request.POST.get(item.item+'_number'):
			cost_of_order += price * int(request.POST.get(item.item+'_number'))
		order_items.append(item)

	order = Order.objects.create(cost_of_order=cost_of_order)

	# Iterate through the order items to create a single order
	for item in order_items:
		take_order = TakeOrder.objects.create(
			item=item, 
			order=order, 
			number_of_items=request.POST.get(item.item+'_number')
			) 
	return take_order

# Make sure you fix the code below ASAP

def pdf_handler(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="Order.pdf"'
	items = ['bread', 'sugar', 'cheese']

	title = "Welcome to my Hotel"
	p = canvas.Canvas(response)
	p.setTitle(title)
	p.setFont('Helvetica', 24)
	p.drawCentredString(3.75*inch, 10.7*inch, 'Welcome to our Hotel')
	p.setFont('Helvetica', 17)
	p.drawCentredString(3.75*inch, 9.7*inch, ' Item    @ Price    Item no.')
	x = 3.75*inch
	y = 9.0*inch
	for item in items:
		p.setFont('Helvetica', 15)
		p.drawCentredString(x, y, item)
		y -= 25
	p.drawCentredString(x,y, "Total Cost : ")
	p.showPage()
	p.save()
	return response