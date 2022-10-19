from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


# def january(request):
#     return HttpResponse("January")


# def february(request):
#     return HttpResponse("February")


# def march(request):
#     return HttpResponse("March")
months = {
    "january": "January",
    "february": "February",
    "march": "March",
    "april": "April",
    "may": "May",
    "june": "June", 
    "july": "July",
    "august": "August",
    'september': "September",
    "octobre": "Octobre",
    "novembre": "Novembre",
    "december" : "December"
}

def monthly_challenge(request, month):
    try:
        text = months[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("This month is not found!")
    

def monthly_challenge_by_number(request, month):
    month_keys = list(months.keys())
    try:
        redirect_month = month_keys[month - 1]
        return HttpResponseRedirect("/challenges/" + redirect_month)
    except:
        return HttpResponseNotFound("This month is not found!")
