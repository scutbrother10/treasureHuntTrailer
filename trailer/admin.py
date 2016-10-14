from django.contrib import admin
from trailer.models import Video, Product

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Video, VideoAdmin)
admin.site.register(Product)
