from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry# 数据库表
        fields = ['entry_title', 'entry_text', 'entry_image'] # 数据库列