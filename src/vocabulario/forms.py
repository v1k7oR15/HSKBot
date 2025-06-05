from django import forms
from django.contrib.auth.models import User
from .models import Palabra, Tipo

class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class PalabraForm(forms.ModelForm):
    palabra = forms.CharField(label='Vocabulario en chino', max_length=10)
    pinyin = forms.CharField(label='Pinyin', max_length=10)
    traduccion = forms.CharField(label='Traducción', max_length=100)
    tipo = forms.ModelChoiceField(
        label='Tipo',
        queryset=Tipo.objects.all(),
        empty_label="Selecciona un tipo"
    )
    nivel_hsk = forms.IntegerField(label='Nivel HSK', min_value=1, max_value=6, required=False)
    ejemplo = forms.CharField(label='Ejemplo', widget=forms.Textarea, required=False)

    class Meta:
        model = Palabra
        fields = ['palabra', 'pinyin', 'traduccion', 'tipo', 'nivel_hsk', 'ejemplo']
