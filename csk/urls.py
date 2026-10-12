from django.urls import path
from csk.views import *
app_name='something'
urlspattern=[
    path('choco/',choco,name='choco'),
]