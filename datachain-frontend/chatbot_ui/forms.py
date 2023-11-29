# chatbot_ui/forms.py

from django import forms

class SQLQueryForm(forms.Form):
    query = forms.CharField(widget=forms.Textarea(attrs={'class': 'sql-input', 'placeholder': 'Enter your SQL query here...'}), label='')
