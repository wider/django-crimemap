from django import forms

class DateRangeForm(forms.Form):
    start_date = forms.DateField(label="Start Date")
    end_date   = forms.DateField(label="End Date")
