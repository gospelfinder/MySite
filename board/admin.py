from django.contrib import admin
from board.models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'owner', 'create_dt', 'hits')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'slug', 'content')
    prepopulated_fields = {'slug': ('title',)}
    
# Register your models here.
