from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'What\'s happening?'}))
    image = forms.ImageField(required=False)

    class Meta:
        model = Tweet
        fields = ['text', 'image']
    