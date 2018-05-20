from django.shortcuts import render,  redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET", "POST"])
def index(request, namepage):
    # we should replace this static with a query on the database
    user_dict = {'user_dict':
                    {
                    'username': str(namepage),
                    'headline': 'GIS developer with a Master of Science (MSc) in Geomatics from Delft University of Technology. Skilled in Python, GIS, FME, Pandas and SQL.',
                    'jobs' : [
                        {'title': 'job 1','period':'1900 - 2017','description':'some description'},
                        {'title': 'job 2','period':'1900 - 2017','description':'some description'},
                        {'title': 'job 3','period':'1900 - 2017','description':'some description'},
                        {'title': 'job 4','period':'1900 - 2017','description':'some description'},
                        {'title': 'job 5','period':'1900 - 2017','description':'some description'},
                        {'title': 'job 6','period':'1900 - 2017','description':'some description'}
                        ]
                    }
                }
    return render(request, "index.html",user_dict)
