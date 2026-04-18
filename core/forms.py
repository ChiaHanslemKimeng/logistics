from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'input input-bordered w-full rounded-xl', 'placeholder': 'your@email.com'}),
            'rating': forms.Select(attrs={'class': 'select select-bordered w-full rounded-xl'}),
            'message': forms.Textarea(attrs={'class': 'textarea textarea-bordered w-full rounded-xl h-32', 'placeholder': 'Share your experience...'}),
        }
