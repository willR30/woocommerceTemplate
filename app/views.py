from django.shortcuts import render, get_object_or_404, redirect
from .models import CategoriaProducto, Producto
from django.http import HttpResponseRedirect
from django.urls import reverse

# Vista para listar categorías y productos
def index(request):
    categorias = CategoriaProducto.objects.all()
    productos = Producto.objects.all()
    return render(request, 'index.html', {'categorias': categorias, 'productos': productos})

# CRUD para Categoría
def agregar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        CategoriaProducto.objects.create(nombre=nombre)
        return redirect('index')
    return render(request, 'agregar_categoria.html')

def editar_categoria(request, id):
    categoria = get_object_or_404(CategoriaProducto, pk=id)
    if request.method == 'POST':
        categoria.nombre = request.POST['nombre']
        categoria.save()
        return redirect('index')
    return render(request, 'editar_categoria.html', {'categoria': categoria})

def eliminar_categoria(request, id):
    categoria = get_object_or_404(CategoriaProducto, pk=id)
    categoria.delete()
    return redirect('index')

# CRUD para Producto
def agregar_producto(request):
    categorias = CategoriaProducto.objects.all()
    if request.method == 'POST':
        Producto.objects.create(
            codigo=request.POST['codigo'],
            nombre=request.POST['nombre'],
            categoria=get_object_or_404(CategoriaProducto, pk=request.POST['categoria']),
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            imagen_url=request.POST['imagen_url'],
        )
        return redirect('index')
    return render(request, 'agregar_producto.html', {'categorias': categorias})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    categorias = CategoriaProducto.objects.all()
    if request.method == 'POST':
        producto.codigo = request.POST['codigo']
        producto.nombre = request.POST['nombre']
        producto.categoria = get_object_or_404(CategoriaProducto, pk=request.POST['categoria'])
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.imagen_url = request.POST['imagen_url']
        producto.save()
        return redirect('index')
    return render(request, 'editar_producto.html', {'producto': producto, 'categorias': categorias})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    return redirect('index')
