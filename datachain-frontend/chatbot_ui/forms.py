# chatbot_ui/forms.py

from django import forms
from django.db import connection

class SQLQueryForm(forms.Form):
    query = forms.CharField(widget=forms.Textarea(attrs={'class': 'sql-input', 'placeholder': 'Enter your SQL query here...'}))

    table = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'table-select'}))

    def __init__(self, *args, **kwargs):
        super(SQLQueryForm, self).__init__(*args, **kwargs)
        self.fields['table'].choices = self.get_table_choices()

    def get_table_choices(self):
        # Replace this with your code to fetch available tables from the SQL server
        # Example:
        with connection.cursor() as cursor:
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            tables = [row[0] for row in cursor.fetchall()]
        return [(table, table) for table in tables]
    


