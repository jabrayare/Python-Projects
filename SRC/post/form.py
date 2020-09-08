from django import forms

from .models import Post

# This creates fields that user can see to submit data to database.


# form validation.
class PostForm(forms.ModelForm):
    Message = forms.CharField(initial='', widget=forms.Textarea(attrs={
        "class": "className",
        "rows": 20,
        "cols": 102
    }))

    class Meta:
        model = Post
        fields = [
            "Name",
            "Message",
            "Email"
        ]

    def clean_Message(self, *args, **kwargs):
        message = self.cleaned_data.get('Message')
        if not "Jabros" in message:
            raise forms.ValidationError("THis is not a valid message")
        return message

    def clean_Email(self, *args, **kwargs):
        email = self.cleaned_data.get("Email")
        if not email.endswith(".edu"):
            raise forms.ValidationError("Not a valid Email")
        return email


class RawProductForm(forms.Form):
    Name = forms.CharField(label='')
    Email = forms.CharField()
    Message = forms.CharField(initial='Your message', widget=forms.Textarea(attrs={
        "class": "className",
        "rows": 20,
        "cols": 102
    }))
