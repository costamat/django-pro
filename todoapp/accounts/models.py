from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    photo = models.ImageField('Foto', upload_to='photos')
    cell_phone = models.CharField('Celular', max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Perfil do usuário'
        verbose_name_plural='Perfis dos usuários'
    
    def __str__(self):
        return self.user.username


class CategoryTest(models.Model):
    name = models.CharField('Nome', max_length=150)
    description = models.TextField('Descrição', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Categoriatest'
        verbose_name_plural = 'Categoriastest'
        ordering = ['id']

    def __str__(self):
        return self.name