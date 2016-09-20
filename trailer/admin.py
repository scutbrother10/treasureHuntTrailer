from django.contrib import admin
from trailer.models import Video

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Video, VideoAdmin)