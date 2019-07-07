from django.shortcuts import render
from .models import Historia
from .forms import HistoriaForm
from django.http import HttpResponse

# Create your views here.

def CrearVistaHistoria(request):
    if request.method == 'POST':
        form = HistoriaForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('HISTORIA GUARDADA')

    else:
        form = HistoriaForm()
    return render(request, 'crearHistoria.html', {'form':form})


from django.views import generic

class detallesDeHistoria(generic.DetailView):
    model = Historia
    template_name = 'historia.html'