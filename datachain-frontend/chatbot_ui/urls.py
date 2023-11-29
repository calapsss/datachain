# chatbot_ui/urls.py

from django.urls import path
from . import views
from .views import database_tables
from .views import view_table
from .views import query_page

urlpatterns = [
    path('', views.index, name='index'),
    path('database_tables/', database_tables, name='database_tables'),
    path('view_table/<str:table_name>/', view_table, name='view_table'),
    path('query/', query_page, name='query_page'),
]
