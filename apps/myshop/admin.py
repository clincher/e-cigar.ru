from django.contrib import admin

from apps.myshop.models import (Manufacturer, Flavour, Accessory, Cigarette,
    Cartridge, CartridgeImage, CigaretteImage, AccessoryImage)


class ProductImageAdmin(admin.TabularInline):
    """
    this class is for set up product admin image classes through one point
    """
    extra = 1


class NameSlug(admin.ModelAdmin):
    """
    this class is for set up all product admin classes through one point
    """
    prepopulated_fields = {"slug": ("name",)}


class CigaretteImageInline(ProductImageAdmin):
    model = CigaretteImage


class CigaretteAdmin(NameSlug):
    inlines = [CigaretteImageInline,]
    class Media:
        js = ('tiny_mce/tiny_mce.js',
              'filebrowser/js/TinyMCEAdmin.js',)


class CartridgeImageInline(ProductImageAdmin):
    model = CartridgeImage


class CartridgeAdmin(NameSlug):
    inlines = [CartridgeImageInline,]
    class Media:
        js = ('tiny_mce/tiny_mce.js',
              'filebrowser/js/TinyMCEAdmin.js',)


class AccessoryImageInline(ProductImageAdmin):
    model = AccessoryImage


class AccessoryAdmin(NameSlug):
    inlines = [AccessoryImageInline,]
    class Media:
        js = ('tiny_mce/tiny_mce.js',
              'filebrowser/js/TinyMCEAdmin.js',)


class FlavourAdmin(NameSlug):
    pass


class ManufacturerAdmin(NameSlug):
    pass


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Flavour, FlavourAdmin)
admin.site.register(Cigarette, CigaretteAdmin)
admin.site.register(Cartridge, CartridgeAdmin)
admin.site.register(Accessory, AccessoryAdmin)