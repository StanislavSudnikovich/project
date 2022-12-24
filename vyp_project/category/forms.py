from django import forms


class ReviewForm(forms.Form):
    author = forms.CharField(
        max_length=68,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваше имя'
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ваш отзыв'
        }
    ))
