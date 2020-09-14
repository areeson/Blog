from django import forms
from blog.models import HomeContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = HomeContactMessage
        fields = ['full_name', 'email', 'content']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        print(email)
        if email.endswith(".edu"):
            raise forms.ValidationError(
                "This is not a valid email. Please don't use .edu.")
        return email
