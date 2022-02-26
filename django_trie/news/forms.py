from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anans', 'text', 'data_time']

        widgets = {
            "title": TextInput( attrs={
                'class': 'form_control',
                'placeholder': "Название поста"
            }),
            "anans": TextInput( attrs={
                'class': 'form_control',
                'placeholder': "Описание поста"
            }),
            "text": Textarea(attrs={
                'class': 'form_control',
                'placeholder': "Текст поста"
            }),
            "data_time": DateTimeInput(attrs={
                'class': 'form_control',
                'placeholder': "Дата и время"
            })
        }
