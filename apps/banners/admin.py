from django.contrib import admin

from models import Banner

class BannerAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny_mce/tiny_mce.js',
              'filebrowser/js/TinyMCEAdmin.js',)


admin.site.register(Banner, BannerAdmin)
