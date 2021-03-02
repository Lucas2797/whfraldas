from django.contrib import admin
from .models import Profile, Vagas, News, NewsImages


class ProfileConfig(admin.ModelAdmin):
    list_display = ('user', 'name', 'last_name', 'phone')


class VagasConfig(admin.ModelAdmin):
    list_display = ('position', 'requirements', 'description', 'active')


class NewsConfig(admin.ModelAdmin):
    list_display = ('headline', 'text', 'date')

class NewsImagesConfig(admin.ModelAdmin):
    list_display = ('new', 'imagem', 'image_text')

admin.site.register(Vagas, VagasConfig),
admin.site.register(Profile, ProfileConfig)
admin.site.register(News, NewsConfig)
admin.site.register(NewsImages, NewsImagesConfig)
