from django.contrib import admin

from models import Article


class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny_mce/tiny_mce.js',
              'filebrowser/js/TinyMCEAdmin.js',)


admin.site.register(Article, ArticleAdmin)
