from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


# def january(request):
#     return HttpResponse("Go gym daily!")

# def february(request):
#     return HttpResponse("Study Django Daily")january

monthly_challenges = {
    "january" : "Go gym daily!",
    "february" : "Study Django Daily",
    "march" : "Get new job!",
    "april" : "Study new skills and keep growing!",
    "may" : "Get a GirlFriend!",
    "june" : "Enjoy atleast once!",
    "july" : "Buy mom a gift atleast this year!",
    "august" : "Hopefully you are shredded with atleast 15% bodyfat",
    "september" : "Do not wish her birthday wish!",
    "october" : "Atleast a 12LPA job at this time!",
    "november" : "Make sure all the above objectives are completed!",
    "december" : "Make sure you had a blast year"
}

def monthly_challenge_by_number(request, month):
    
    monthList = list(monthly_challenges.keys())
    print("Check")
    if(month>len(monthList)):
        return HttpResponseNotFound("This month is Invalid!")
    redirect_Month = monthList[month-1]
    redirect_Path = reverse("month-challenge",args=[redirect_Month]) #first-arg comes from urls.py where we pass /challenges and 2nd argument we need to pass what is the final endpoint

    

    # return HttpResponseRedirect("/challenges/"+ redirect_Month)
    return HttpResponseRedirect(redirect_Path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is invalid!")
    return HttpResponse(challenge_text)