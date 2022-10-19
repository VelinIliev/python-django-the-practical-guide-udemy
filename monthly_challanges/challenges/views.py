from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "december" : None
}

def index(request):
    months_list = ""
    for month in months.keys():
        month_path = reverse("month-challenge", args=[month])
        months_list += f'<li><a href="{month_path}">{month.capitalize()}</a></li>\n'
    response_data = f'<ul>\n{months_list}</ul>'
    return render(request, "challenges/index.html", {
        "months": list(months.keys())
    })


def monthly_challenge(request, month):
    try:
        text = months[month]
        return render(request, "challenges/challenge.html", {
            "text": text,
            "month_name": month,
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not found!</h1>")
    

def monthly_challenge_by_number(request, month):
    month_keys = list(months.keys())   
    try:
        redirect_month = month_keys[month - 1]
        redirect_path = reverse("month-challenge",  args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("<h1>This month is not found!</h1>")

