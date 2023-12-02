from django.db import models

class Contact(models.Model):
    name = models.CharField('Имя', max_length=50)
    age = models.CharField('Сколько лет', max_length=250)
    tel = models.CharField('Номер телефона', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'