from django.contrib import admin
from .models import Camaras, Category, Sector, Fornecedores


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = (
        'code', 
        'sector',
    )

    search_fields = ('code', 'sector')
    list_filter = (
        'code',
        'sector',
    
    )


@admin.register(Camaras)
class CamarasAdmin(admin.ModelAdmin):
    list_display = (
        'code', 
        'name', 
        'location', 
        'operation_status', 
        'min_temperature',
        'max_temperature', 
        'min_humidity', 
        'max_humidity', 
        'description'
    )
    
    search_fields = ('code', 'name')
    list_filter = (
        'code',
        'name',
        'operation_status'
    
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'code', 
        'name', 
        'description',
    )

@admin.register(Fornecedores)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = (
        'code', 
        'name', 
        'email', 
        'cnpj', 
        'status',
    )