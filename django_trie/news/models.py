from django.db import models

# Create your models here.


class Articles(models.Model):
    object = ''
    title = models.CharField('Название', max_length=50)
    anans = models.CharField('Анонс', max_length=250)
    text = models.TextField('Текст')
    data_time = models.DateTimeField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

