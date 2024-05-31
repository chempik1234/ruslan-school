from django import forms
from .models import User


class SignInForm(forms.Form):
    email = forms.EmailField(label='Почта', required=True,
                             max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', required=True,
                               max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # remember_me = forms.BooleanField(label='Запомнить меня', required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователя с такой почтой нет!")
        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Логин не прошёл проверку!")
        password = self.cleaned_data['password']
        found_user = User.objects.get(email=email)
        if not found_user.check_password(password):
            raise forms.ValidationError("Неверный пароль!")
        return password


class SignUpForm(forms.Form):
    email = forms.EmailField(label='Почта', required=True,
                             max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.EmailField(label='Имя', required=True,
                                  max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.EmailField(label='Фамилия', required=True,
                                 max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', required=True,
                               max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # remember_me = forms.BooleanField(label='Запомнить меня', required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с такой почтой уже есть!")
        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Логин не прошёл проверку!")
        password = self.cleaned_data['password']
        return password

    def save(self):
        data = self.cleaned_data
        new_user = User()
        new_user.email = data.get('email')
        new_user.first_name = data.get('first_name')
        new_user.last_name = data.get('last_name')
        new_user.set_password(data.get('password'))
        new_user.save()
        return new_user


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Почта", help_text="Почта, на которую придёт новый пароль",
                             required=True, max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователя с такой почтой нет!")
        return email


class EmailForm(forms.Form):
    email = forms.EmailField(label='Почта', required=True,
                             max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))


class AvatarForm(forms.Form):
    avatar = forms.ImageField(required=True)
