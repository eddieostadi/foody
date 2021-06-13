from django import forms
from django.forms import TextInput

from .models import User, SpecialDiet, Food


class LoginForm(forms.Form):
    username = forms.CharField(empty_value=False, label='username', max_length=30)
    password = forms.CharField(empty_value=False, label='password', max_length=25, widget=forms.PasswordInput)


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'sex', 'age', 'weight', 'height', 'password']

    password2 = forms.CharField(label='repeat password', required=True)


    def valid_password(self):
        if self.cleaned_data["password"] == self.data["password2"]:
            user = super(NewUserForm, self).save(commit=False)

            return True
        else:

            return False

class Qform(forms.Form):
    #title= forms.CharField(max_length=30, required=False, label="Food Name")
    DIET_CHOICE = [('vegan', 'vegan'), ('vegetarian', 'vegetarian'), ('wheat/gluten-free', 'wheat/gluten-free'),
                   ('diary free', 'diary free'), ('seafood', "seafood")]
    diet = forms.MultipleChoiceField(choices=DIET_CHOICE, widget=forms.CheckboxSelectMultiple())