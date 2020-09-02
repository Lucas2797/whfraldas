from django.contrib import admin
from .models import Banner, BannerImages, Contact


class ContactConfig(admin.ModelAdmin):
    list_display = ('nome', 'phone', 'email')


class BannerConfig(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'url')


class BannerImagesConfig(admin.ModelAdmin):
    list_display = ('banner', 'imagem')


admin.site.register(Banner, BannerConfig),
admin.site.register(BannerImages, BannerImagesConfig),
admin.site.register(Contact, ContactConfig)