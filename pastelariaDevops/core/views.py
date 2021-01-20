from django.shortcuts import render
from django.shortcuts import redirect
from .models import Loja
from .forms import LojaForm

# Create your views here.

def read_loja(request):
    lojas = Loja.objects.all()
    return render(request, 'loja_lista.html', {"lojas": lojas})

def create_loja(request):
    form = LojaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        #return render(request, 'loja_obrigado.html')
        return redirect('read_loja')
    return render(request, 'loja_form.html', {"form": form})
