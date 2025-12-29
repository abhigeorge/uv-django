from django.contrib import admin
from django.utils.html import format_html
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_at", "image_preview")
    list_filter = ("uploaded_at",)
    search_fields = ("title",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Preview"