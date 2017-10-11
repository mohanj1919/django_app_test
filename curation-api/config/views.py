from django.shortcuts import render
from django.conf import settings

def index(request, path=''):
    """
    Renders the React Single Page App
    """
    # import pdb;pdb.set_trace()
    return render(request, 'index.html')
