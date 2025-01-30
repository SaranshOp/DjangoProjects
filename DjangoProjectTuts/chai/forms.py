from django import forms
from .models import ChaiVariety

class ChaiVarietyForm(forms.Form):
    variety = forms.ModelChoiceField(
        queryset=ChaiVariety.objects.all(),
        label='Select Chai Variety'
    )

    # class Meta:  # This was the missing in my code! need to search
    #     model = ChaiVariety
    #     fields = ['chai_type']
