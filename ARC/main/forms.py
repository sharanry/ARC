from django import forms
from main.models import Map


class MapsForm(forms.Form):
    Course_Map = forms.ModelMultipleChoiceField(
        queryset=Map.objects.all(),
        required=True,
        help_text='Which pre-defined map to apply?',
    )
