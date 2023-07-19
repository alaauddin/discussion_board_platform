from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class YearSelectWidget(forms.Select):
    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs, choices)
        self.choices = choices


class SignUpForm (UserCreationForm):
    email = forms.CharField(max_length=255, required=True,widget=forms.EmailInput())
    age = forms.IntegerField(widget=forms.NumberInput())
    department = forms.CharField(max_length=100,required=True)

    year_choices = [
        ('FE', 'FE'),
        ('SE', 'SE'),
        ('TE', 'TE'),
        ('BE', 'BE'),
    ]
    year = forms.ChoiceField(choices=year_choices, widget=forms.Select())

    roll_number = forms.CharField(
        max_length=10,
        help_text='Enter roll number in the format e.g. CS-YYXXX',
        validators=[RegexValidator(r'^[A-Z]{2}-\d{5}$', 'Invalid roll number format.')]
    )

    class Meta:
        model=User
        fields = {'username','email','age','department','year', 'password1', 'password2','roll_number'}