from django.contrib import admin
from .models import Comment

# Register your models here.

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'formatted_datePost', 'element')
    search_fields = ('id',)
    date_hierarchy = 'date_posted'
    ordering = ('-date_posted',)
    list_filter = ('id','date_posted')
    # list_editable = ('text',)

    def delete_queryset(self, request, queryset):
        print('delete_queryset-Antes')
        super().delete_queryset(request, queryset)
        print('delete_queryset-Despues')    
        
    def save_model(self, request, obj, form, change):
        print('save_model-Antes')
        super().save_model(request, obj, form, change)
        print('save-model -despues')
        
    class Media:
        css ={'all':['comments/my_stile.css']}