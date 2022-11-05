from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
	obj = models.Bus.objects.first()
	field_names = [f.name for f in obj._meta.get_fields()]
	f = field_names.value_from_object(obj)
	name = 'Relâmpago Marquinhos'
	context = {
		'n': name,
		'm': 'Mensagem',
	}
	# context['speed'] = a.get_speed()
	return render(request, 'index.html', context)
    #return HttpResponse("Hello, world. You're at the bus tracker index.")