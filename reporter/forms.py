from django import forms

from .models import Report , InformationList

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title','content']

class DeadlineForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type':'datetime-local','class': 'form-control-sm'})
        }
        labels = {
            'deadline': ''
        }


class InformationListForm(forms.ModelForm):
    class Meta:
        model = InformationList
        fields=['name','course','email','phone']