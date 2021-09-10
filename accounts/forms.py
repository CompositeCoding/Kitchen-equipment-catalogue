# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.mail import send_mail

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username','email','kvk','Telefoon','Adres','Huisnummer','Postcode',)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'size':'30'})
        self.fields['Telefoon'].widget.attrs.update(required=False)
        self.fields['kvk'].widget.attrs.update(required=False)
        self.fields['username'].label = "Bedrijfsnaam"
        self.fields['password1'].label = "Wachtwoord"
        self.fields['password2'].label = "Herhaal Wachtwoord"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','kvk','Telefoon')


class ContactForm(forms.Form):
    Bedrijfsnaam = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    Email = forms.EmailField(required=True,  widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    Telefoon = forms.CharField(required=True,label='Telefoonnummer', widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    Contact = forms.ChoiceField(choices=(("1.", "Telefoon"),("2.","Email")), required=True, label="Contact opnemen via")
    Bericht = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': 15, 'cols': 40})
    )

    def send_email(self):
        data = self.cleaned_data
        emailadres = data['Email']
        naam = data['Bedrijfsnaam']
        telefoon = data['Telefoon']
        if data['Contact'] == "1.":
            manier = "Telefoon"
        else:
            manier = "Email"
        bericht = data['Bericht']
        send_mail(f'Automatisch bericht na invullen contactformulier website',f"Dit is een automatisch bericht van de website nadat een klant een contactformulier heeft ingevuld:\n\n\n Dit is een bericht van {naam}.\nDe gewenste manier van contact is via {manier} \nEmail = {emailadres} \nTelefoon = {telefoon} \n\nBericht van Klant: \n\n{bericht} " , 'casper-vliet@hotmail.com', ["casper-vliet@hotmail.com"], fail_silently=False)
