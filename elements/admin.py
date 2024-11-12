from django.contrib import admin
from .models import Category, Type, Element
from django.utils.text import slugify

# Register your models here.

@admin.register(Category, Type)
class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug')

@admin.display(description="ID and Title in UpperCase")
def upper_title(obj):
    return f"{obj.id} - {obj.title}".upper()
    
@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    
    list_display = ('id','title', 'slug', 'category', 'type','adminCreateDate',upper_title,'cheap')
    readonly_fields = ('adminCreateDate','adminUpdateDate')
    #fields = (('title','slug'),'description', 'price', ('category', 'type'))
    fieldsets = (
        ('General', {
            'classes': ('form-row',),  # Usamos form-row para organizar en una sola fila
            'fields': (('title', 'slug'),)
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Price', {
            'fields': ('price',)
        }),
        ('Category and Type', {
            'classes': ('form-row',),
            'fields': (('category', 'type'),)
        }),
        ('Date Information', {
            'fields': ('adminCreateDate', 'adminUpdateDate')
        }),
    )
    list_filter = ('category', 'type')
    ordering = ('-create',)
    
    def save_model(self, request, obj, form, change):

        if not(change) and obj.slug == '':
            obj.slug = slugify(obj.title)

        if obj.slug == '':
            obj.slug = slugify(obj.title)

        super().save_model(request, obj, form, change)

    
    