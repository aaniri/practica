from .models import Contact
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'age', 'tel']

        widgets = {
            "name":TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Ваше имя'
            }),
            "age":TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Укажите возраст'
            }),
            "tel":TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Телефон: +7999999999'
            }),
    
        }