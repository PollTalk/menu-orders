# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, RequestContext, loader 
from .models import Item

def index(request):
	latest_items = Item.objects.all().order_by('-date_created')[:5]
	template = loader.get_template('orders/index.html')
	context = RequestContext(request, {
        'latest_items': latest_items,
        })
	return HttpResponse(template.render(context))
