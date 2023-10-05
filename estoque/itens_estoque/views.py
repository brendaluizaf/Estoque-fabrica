from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemEstoque
from .forms import ItemEstoqueForm

def lista_estoque(request):
    itens = ItemEstoque.objects.all()
    return render(request, 'itens_estoque/lista_estoque.html', {'itens': itens})

def adicionar_item(request):
    # Lógica para adicionar um novo item
    if request.method == 'POST':
        form = ItemEstoqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estoque')
    else:
        form = ItemEstoqueForm()
    return render(request, 'itens_estoque/adicionar_item.html', {'form': form})

def detalhes_item(request, id):
    # Lógica para exibir detalhes de um item específico
    item = get_object_or_404(ItemEstoque, pk=id)
    return render(request, 'itens_estoque/detalhes_item.html', {'item': item})

def editar_item(request, id):
    # Lógica para editar um item específico
    item = get_object_or_404(ItemEstoque, pk=id)
    if request.method == 'POST':
        form = ItemEstoqueForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('detalhes_item', id=id)
    else:
        form = ItemEstoqueForm(instance=item)
    return render(request, 'itens_estoque/editar_item.html', {'form': form, 'item': item})

def verificar_exclusao(request, id):
    # Lógica para confirmar a exclusão de um item
    item = get_object_or_404(ItemEstoque, pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('lista_estoque')
    return render(request, 'itens_estoque/verificar_exclusao.html', {'item': item})
