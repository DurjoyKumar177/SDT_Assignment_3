from django import forms
from django.utils.safestring import mark_safe
from django.forms.widgets import NumberInput
import datetime
from .models import MyModel

# Predefined choices for birth years and favorite colors
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class ExampleForm(forms.Form):
    # A text area for general comments
    comment = forms.CharField(widget=forms.Textarea)

    # Another comment field with a custom row size
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    # Email input field
    email = forms.EmailField()

    # First heading with custom styling (readonly, bold)
    heading1 = forms.CharField(
        label='',  # No label
        widget=forms.TextInput(attrs={  # Customize text input
            'readonly': 'readonly',  # Prevent editing
            'style': 'border:none; font-weight:bold; font-size:16px; margin-top:20px;'  # Add margin-top for spacing
        }),
        initial='Please fill the form below:',  # Default text
    )

    # A Boolean checkbox field for user agreement
    agree = forms.BooleanField()

    # A standard date field
    date = forms.DateField()

    # Date input field with custom widget (date picker)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    # Date picker with year choices
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    # Decimal input field
    value = forms.DecimalField()

    # Another heading with custom styling
    heading2 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'readonly': 'readonly',
            'style': 'border:none; font-weight:bold; font-size:16px; margin-top:20px;'  # Add margin-top for spacing
        }),
        initial=mark_safe('Core Arguments with Condition'),
    )

    # Optional email field
    email_address = forms.EmailField(required=False)

    # Short text field with max length of 10 characters
    message = forms.CharField(max_length=10)

    # Email field with label
    email_address = forms.EmailField(label="Please enter your email address")

    # Text input field with default value
    first_name = forms.CharField(initial='Your name')

    # Date field with today's date as default
    day = forms.DateField(initial=datetime.date.today)

    # Heading for choice section
    heading3 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'readonly': 'readonly',
            'style': 'border:none; font-weight:bold; font-size:16px; margin-top:20px;'  # Add margin-top for spacing
        }),
        initial=mark_safe('Select Your Choice: '),
    )

    # Radio button field for selecting a single favorite color
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)

    # Heading for multiple choice section
    heading4 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'readonly': 'readonly',
            'style': 'border:none; font-weight:bold; font-size:16px; margin-top:20px;'  # Add margin-top for spacing
        }),
        initial=mark_safe('Select Your Multiple Choice: '),
    )

    # Multiple choice field with checkboxes for selecting multiple colors
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)

    # Heading for model choice section
    heading5 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'readonly': 'readonly',
            'style': 'border:none; font-weight:bold; font-size:16px; margin-top:20px;'  # Add margin-top for spacing
        }),
        initial=mark_safe('Choose Models: '),
    )

    # Dropdown field for selecting a single model from the queryset
    model_choice = forms.ModelChoiceField(queryset=MyModel.objects.all(), initial=0)

    # Checkbox field for selecting multiple models from the queryset
    model_choices = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=MyModel.objects.all(), initial=0)
