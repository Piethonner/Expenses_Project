from django import forms
from .models import Expense


class ExpenseSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    class Meta:
        model = Expense
        fields = ('name',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['start_date'].required = False
        self.fields['end_date'].required = False
        
