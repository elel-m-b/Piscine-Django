from django import forms


class InputForm(forms.Form):
    """A simple form with a single text field, as required by the subject.

    The field is defined here (in forms.py) instead of being hard-coded
    in the template, so Django takes care of rendering, validation and
    the CSRF-protected widget for us.
    """
    user_input = forms.CharField(
        label='',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Type something...'}),
    )
