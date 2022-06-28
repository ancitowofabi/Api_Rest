from email.mime import image
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item,Cliente
from .forms import ItemForm,ClienteForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def somos(request):
    return render(request, 'somos.html')

def contacto(request):
    return render(request, 'contacto.html')

def galeria(request):
    items = Item.objects.all()
    datos= {
        'items' : items
    }
    return render(request, 'galeria.html', datos)

def register(request):
    return render(request, 'register.html')

def imc(request):
    return render(request, 'imc.html')

def inspirate(request):
    return render(request, 'inspirate.html')

def login(request):
    return render(request, 'login.html')
    
def form_crear_item(request):
    return render(request, 'form_crear_item.html')
   
    #mostrar los objetos almacenados de la clase item
def mostrar_item (request):
    items = Item.objects.all()

    datos= {
        'items' : items,
        'item_form': ItemForm()
    }
    return render(request, 'mostrar_item.html', datos)

#crear un objeto de tipo item
def form_crear_item(request):
    if request.method=='POST': 
        item_form = ItemForm(request.POST,request.FILES)
        if item_form.is_valid:
            item_form.save()
            return redirect ('mostrar_item')
    else:
        item_form = ItemForm()
    return render(request, 'form_crear_item.html', {'item_form': item_form})

#modificar un objeto de tipo item
def form_mod_item(request,id):
    item = Item.objects.get(name=id)
    datos={
        'mod_form': ItemForm(instance=item)
    }
    if request.method=='POST':
        formulario=ItemForm(request.POST,request.FILES, instance=item)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar_item')
    
    return render(request, 'form_mod_item.html', datos)


def form_del_item(request, id):
    item = Item.objects.get(name=id)
    item.delete()
    return redirect('mostrar_item')

    
def mostrar_cliente (request):
    cliente = Cliente.objects.all()

    datos= {
        'cliente' : cliente,
        'cliente_form': ClienteForm()
    }
    return render(request, 'mostrar_cliente.html', datos)

#crear un objeto de tipo item
def form_crear_cliente(request):
    if request.method=='POST': 
        cliente_form = ClienteForm(request.POST,request.FILES)
        if cliente_form.is_valid:
            cliente_form.save()
            return redirect ('mostrar_cliente')
    else:
        cliente_form = ClienteForm()
    return render(request, 'form_crear_cliente.html', {'cliente_form': cliente_form})

#modificar un objeto de tipo item
def form_mod_cliente(request,id):
    cliente = Cliente.objects.get(name=id)
    datos={
        'form_mod_cliente': ClienteForm(instance=cliente)
    }
    if request.method=='POST':
        formulario=ClienteForm(request.POST,request.FILES, instance=cliente)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar_cliente')
    
    return render(request, 'form_mod_cliente.html', datos)


def form_del_cliente(request, id):
    cliente = Cliente.objects.get(name=id)
    cliente.delete()
    return redirect('mostrar_cliente')

