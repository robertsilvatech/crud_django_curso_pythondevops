from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
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

def update_loja(request, id):
    loja = get_object_or_404(Loja, pk=id)
    print(loja)
    form = LojaForm(request.POST or None, request.FILES or None, instance=loja)
    print(form)

    if form.is_valid():
        form.save()
        return redirect('read_loja')
    return render(request, 'loja_form.html', {"form": form})

def delete_loja(request, id):
    loja = get_object_or_404(Loja, pk=id)
    form = LojaForm(request.POST or None, request.FILES or None, instance=loja)
    if request.method == 'POST':
        loja.delete()
        return redirect('read_loja')
    return render(request, 'loja_delete_confirm.html', {'form': form, 'loja': loja})
