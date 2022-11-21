from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Gasto, calendario

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'description']

class NuevoGasto(forms.ModelForm):
	class Meta:
		model = Gasto
		exclude = ["xd"]

		
class lista(forms.ModelForm):
	titulo = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Cuenta a pagar'}), label=False)
	fecha = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Fecha de pago.'}), label=False)
	class Meta:
		model = calendario
		fields = ['titulo', 'fecha']

class actualizarform(forms.ModelForm):
	titulo = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}))

	class Meta:
		model = calendario
		fields = ['titulo', 'fecha', 'hecho']