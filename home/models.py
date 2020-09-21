from django.db import models
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField
from .managers import BannerManager


INICIAL= 'INICIAL'
ICONS = 'ICONS'
PRODUTO = 'PRODUTO'

banner_choices = [
        (INICIAL, 'INICIAL'),
        (ICONS, 'ICONS'),
        (PRODUTO, 'PRODUTO')
    ]


class Banner(models.Model):
    nome = models.CharField(max_length=100, default='lucas')
    tipo = models.CharField(choices=banner_choices, max_length=9)
    text = models.TextField(max_length=500)
    url = models.URLField(null=True)
    front_page = models.BooleanField(default=False)
    objects = BannerManager()

    def __str__(self):
        return '{} - {}'.format(self.nome, self.tipo)


    def get_first_img(self):
        return self.banner_images.first()


def get_image_filename(instance, filename):
    nome = instance.banner.nome
    slug = slugify(nome)
    return "banner_imagens/%s-%s" % (slug, filename)


class BannerImages(models.Model):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE, related_name='banner_images')
    imagem = models.ImageField(upload_to=get_image_filename)
    image_text = models.TextField(max_length=500)


class Contact(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    text = models.TextField()






