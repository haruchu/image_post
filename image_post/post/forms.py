from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    title=forms.CharField(max_length=15)
    image=forms.ImageField()

    class Meta:
        model = Image
        fields = ("title", "image")
