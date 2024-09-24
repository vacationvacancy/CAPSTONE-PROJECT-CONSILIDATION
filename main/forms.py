from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):

    """
    Custom user registration form that extends Django's ModelForm.

    This form is used to register new users, with additional fields for password 
    confirmation and an optional checkbox for receiving emails about development 
    updates and game news.
    """

    password = forms.CharField(widget=forms.PasswordInput)

    """
    Field for the user's password input. The 'PasswordInput' widget ensures that 
    the password is masked when entered.

    :type: str
    """


    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    """
    Field for confirming the password input by the user. Also uses the 'PasswordInput'
    widget for masking the input.

    :type: str
    """


    receive_emails = forms.BooleanField(required=False, label="Would you like to receive emails on dev updates and game news?")

    """
    Optional checkbox for users to indicate whether they'd like to receive emails 
    about updates and news related to the project. Defaults to unchecked.

    :type: bool
    """


    class Meta:

        """
        Meta class that defines the model and fields for the form.
        """
        model = User
        fields = ['username', 'email', 'password', 'password2']
        """
        Fields to be included in the form: username, email, password, and password confirmation.
        :type: list[str]
        """


    def __init__(self, *args, **kwargs):

        """
        Overrides the default initialization to customize the form.
        Removes the default help text for the username field.
        """

        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None

    def clean(self):

        """
        Custom validation method to check if the two password fields match.

        :return: Cleaned form data if validation succeeds.
        :raises forms.ValidationError: If the passwords do not match.
        """
        
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
