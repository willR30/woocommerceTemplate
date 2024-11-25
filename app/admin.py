from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import CategoriaProducto, Producto

# Crear un recurso para cada modelo
class CategoriaProductoResource(resources.ModelResource):
    class Meta:
        model = CategoriaProducto

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

# Registrar el modelo CategoriaProducto con exportación habilitada
@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    resource_class = CategoriaProductoResource  # Vincula el recurso

# Registrar el modelo Producto con exportación habilitada
@admin.register(Producto)
class ProductoAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'categoria', 'precio', 'stock')
    search_fields = ('codigo', 'nombre')
    list_filter = ('categoria',)
    resource_class = ProductoResource  # Vincula el recurso
