# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404

def index(request):
	text = "Welcome to the orders application"
	return HttpResponse(text)
