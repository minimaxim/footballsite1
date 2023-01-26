from django.forms import ModelForm, EmailField, CharField, TextInput, EmailInput, Textarea

from .models import Contact, Comment


class ContactForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Name'
            }
        ),
        max_length=64
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Email'
            }
        ),
        max_length=254
    )
    message = CharField(
        widget=Textarea(
            attrs={
                'class': 'form-control',
                'id': 'message',
                'style': 'height: 12rem',
                'placeholder': 'Message'
            }
        ),
        max_length=1024
    )

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')


class CommentForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-group',
                'id': 'name',
                'placeholder': 'Name'
            }
        ),
        max_length=64
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'form-group',
                'id': 'email',
                'placeholder': 'Email'
            }
        ),
        max_length=254
    )
    message = CharField(
        widget=Textarea(
            attrs={
                'class': 'form-group',
                'id': 'message',
                'style': 'height: 12rem',
                'placeholder': 'Message'
            }
        ),
        max_length=1024
    )

    class Meta:
        model = Comment
        fields = ('name', 'email', 'message')
