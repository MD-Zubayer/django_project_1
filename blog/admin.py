from django.contrib import admin
from .models import Post, Book, Author, FieldType

# Register your models here.
admin.site.register(Post)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'price')
    search_fields = ('title', 'author')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email','title')

@admin.register(FieldType)
class FieldTypeAdmin(admin.ModelAdmin):
    list_display = ('char_field', 'integer_field', 'email', 'url', 'created_at_dt', 'created_at_date', 'created_at_time', 'updated_at', 'boolean_field', 'text_field', 'float_field', 'decimal_field', 'image', 'file')
    search_fields = ('char_field', 'email', 'url')
    list_filter = ('boolean_field',)
    ordering = ('-created_at_dt',)