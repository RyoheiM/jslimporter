from django import forms
from .models import Bunch


class BunchForm(forms.ModelForm):

    class Meta:
        model = Bunch
        fields = ('categoryname', 'chaptername', 'sectionname', 'termname',)
        labels = {
            'categoryname': '部タイトル',
            'chaptername': '章タイトル',
            'sectionname': '節タイトル',
            'termname': '項タイトル',
        }
