from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст статьи', max_length=3000)
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Comments(models.Model):
    
    article = models.ForeignKey(Articles, on_delete = models.CASCADE, related_name='comments_article')
    name = models.CharField('Автор коммеентария', max_length=50)
    full_text = models.TextField('Текст комментаряи', max_length=1000)
    create_date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name ='Комментарий'
        verbose_name_plural ='Комментарии'
    