from django.contrib import admin
from .models import Category, Task

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Task)    
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'owner', 'due_date', 'completed', 'priority']