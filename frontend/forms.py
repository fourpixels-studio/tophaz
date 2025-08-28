from django import forms
from .models import Bookings
from django_recaptcha.fields import ReCaptchaField


class BookingsForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Bookings
        fields = ("__all__")

    def clean_captcha(self):
        captcha_value = self.cleaned_data.get('captcha')
        if not captcha_value:
            raise forms.ValidationError("Please complete the captcha.")
        return captcha_value
