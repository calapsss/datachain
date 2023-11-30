# chatbot_ui/views.py

from django.shortcuts import render
from django.db import connection
from .forms import SQLQueryForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datachain_backend.sqlchain import SQLChain



def index(request):
    return render(request, 'chatbot_ui/index.html')

def database_tables(request):
    # Fetch the list of tables in the database
    with connection.cursor() as cursor:
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        tables = [row[0] for row in cursor.fetchall()]

    return render(request, 'chatbot_ui/database_tables.html', {'tables': tables})

def view_table(request, table_name):
    # Fetch the data from the selected table
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

    # Make sure to return 'columns' in the context
    return render(request, 'chatbot_ui/view_table.html', {
        'rows': rows,
        'columns': columns,
        'table_name': table_name
    })



def query_page(request):
    form = SQLQueryForm(request.POST or None)
    page = request.GET.get('page', 1)
    per_page = 10
    columns, rows = [], []

    if request.method == 'POST' and form.is_valid():
        query = form.cleaned_data['query']
        table = form.cleaned_data['table']

        #Prompt to query with sqlchain
        sqlchain = SQLChain()
        sqlchain.connect()
        query = sqlchain.create_query(query, table, "gpt-3.5-turbo-1106")
        
       
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
            except Exception as e:  # Be more specific with exception handling
                rows = []
                # Handle the exception or display it in the template
  
    paginator = Paginator(rows, per_page)
    try:
        rows = paginator.page(page)
        # Do not forget to add this line to keep track of column headers for each page
        # If rows is a Page object, you may need to adjust how you send columns
    except PageNotAnInteger:
        rows = paginator.page(1)
    except EmptyPage:
        rows = paginator.page(paginator.num_pages)

    # The context now includes 'columns', which is used to display column names in the template
    return render(request, 'chatbot_ui/query_page.html', {
        'form': form,
        'columns': columns,
        'rows': rows,
    })