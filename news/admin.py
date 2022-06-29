from django.contrib import admin
from .models import Editor,Article,tags,photos

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    
# Register your models here.
admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)
admin.site.register(photos)
