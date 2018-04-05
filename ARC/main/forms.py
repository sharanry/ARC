from django import forms
from main.models import Map


class MapsForm(forms.Form):
    Course_Map = forms.ModelMultipleChoiceField(
        queryset=Map.objects.all(),
        required=True,
        help_text='Which pre-defined map to apply?',
    )

class SingleCDCForm(forms.Form):
	# YEAR_CHOICES=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
	# SEM_CHOICES=(('1','1'),('2','2'))
	Year = forms.IntegerField(
        # choices=SEM_CHOICES,
        required=True,
        help_text='Year',
    )

	Sem = forms.IntegerField(  
    	# choices=SEM_CHOICES,
        required=True,
        help_text='Sem',
    )