# Generated by Django 4.2.7 on 2023-11-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dateNews', '0003_alter_articles_full_text_alter_comments_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='full_text',
            field=models.TextField(max_length=3000, verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='full_text',
            field=models.TextField(max_length=1000, verbose_name='Текст комментаряи'),
        ),
    ]
