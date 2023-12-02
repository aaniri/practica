from .models import Articles, Comments
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class AddNews(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title":TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Название статьи'
            }),
                "anons":TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Анонс'
            }),
                "date":DateTimeInput(attrs={
                'class': 'form__input',
                'placeholder': 'Введите дату в формате 2020-12-24 20:20'
            }),
                "full_text":Textarea(attrs={
                'class': 'form__textarea',
                'placeholder': 'Текст статьи'
            }),
        
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'full_text']

        widgets = {
            "name":TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Введите ваше имя'
            }),
                "full_text":Textarea(attrs={
                'class': 'form__textarea',
                'placeholder': 'Введите ваш комментарий'
            }),
        
        }

