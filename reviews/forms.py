from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','comment']
        widgets = {
            'comment' : forms.Textarea(attrs={
                'class': 'bg-gray-800 text-white w-full p-4 rounded-lg border border-gray-700',
                'placeholder': 'Escreva sua review aqui...',
                'rows': 4
            }),
            'rating': forms.Select(attrs={
                'class' : 'bg-gray-800 text-white p-2 rounded border border-gray-700'
            }),
        }