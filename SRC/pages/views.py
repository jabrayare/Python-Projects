from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(requests, *args, **kwargs):
    print(requests.user, 'is logged in')
    print(args, kwargs)
    return render(requests, "home.html", {})


def contact_view(requests, *args, **kwargs):

    return render(requests, "contact.html", {})


def about_view(requests, *args, **kwargs):
    my_context = {
        "my_text": "My name is Jibril. I love coding",
        "my_number": 1234,
        "my_list": [
            1234, 7840, 8932, 99032
        ]
    }
    return render(requests, "about.html", my_context)
