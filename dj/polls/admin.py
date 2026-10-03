from django.contrib import admin

# Register your models here.
from .models import BlogPost, Task

admin.site.register(BlogPost)
# admin.site.register(Task)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "status",
        "description",
        "priority",
        "email"
    )
    search_fields = (
        "description",
        "email"
    )
    list_filter = (
        "status",
        "priority",
    )