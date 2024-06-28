from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)} #из поля title делаем поле slug в реальном времени при помощи JS
    raw_id_fields = ['author'] # позволяет отображения связанных объектов в виде текстового поля
    date_hierarchy = 'publish'# иерархической навигации по датам
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS # отображать фильтры в панели администратора


