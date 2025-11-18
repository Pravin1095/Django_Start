from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


# def january(request):
#     return HttpResponse("Go gym daily!")

# def february(request):
#     return HttpResponse("Study Django Daily")

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    challenge_text = None
    if(month=='january'):
        challenge_text = "Go gym daily!"
    elif(month=='february'):
        challenge_text = "Study Django Daily"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)