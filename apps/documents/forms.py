from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model  = Document
        fields = ['process', 'number', 'title', 'doc_type', 'file']

    def clean_file(self):
        f = self.cleaned_data['file']
        if f.size > 25 * 1024 * 1024:
            raise forms.ValidationError("Файл больше 25 MB")
        return f
