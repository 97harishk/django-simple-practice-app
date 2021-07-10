from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def index(request):
    meetups = [
        {
            "id": 1,
            "name": "Harish Kumar"
        },
        {
            "id": 2,
            "name": "Ankit Kumar"
        },
        {
            "id": 3,
            "name": "Amit Kumar"
        }

    ]
    return render(request, 'meetups/index.html', {
        "show": False,
        "meetups": meetups
    })