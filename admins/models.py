from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import slugify


User = get_user_model()



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='profile')
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneNumberField()


    def __str__(self):
        return self.user, '-', self.name, self.last_name
    



class Vagas(models.Model):
    profiles = models.ManyToManyField(Profile, related_name='profs', blank=True)
    position = models.CharField(max_length=100)
    requirements = models.TextField(max_length=400)
    description = models.TextField(max_length=400)
    active = models.BooleanField(default=False)



class News(models.Model):
    headline = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        dating = slugify(self.date.date())
        return self.headline + '-' + dating


def get_image_filename(instance, filename):
    nome = instance.new.headline[:30]
    slug = slugify(nome)
    return "banner_imagens/%s-%s" % (slug, filename)


class NewsImages(models.Model):
    new = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_images')
    imagem = models.ImageField(upload_to=get_image_filename)
    image_text = models.TextField(max_length=500)

