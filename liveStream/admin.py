from django.contrib import admin
from liveStream.models import LiveStream, ContactDetail
from django.utils.html import format_html

# Register your models here.
class LiveStreamAdmin(admin.ModelAdmin):
    list_display = ('title', 'stream_key', 'collect_details', 'export_url')
    
    def export_url(self, obj):
        return format_html(f"<a href='/export/{obj.stream_key}' target='_blank'>/export/{obj.stream_key}</a>")
    export_url.allow_tags = True
    export_url.short_description = "Export URL"

admin.site.register(LiveStream, LiveStreamAdmin)

#admin.site.register(LiveStream)
admin.site.register(ContactDetail)

