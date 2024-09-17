from django.contrib import admin
from .models import Book
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "subtitle",
        "auther",
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Default filter: only show unread messages
        return qs.filter(is_read=False)
