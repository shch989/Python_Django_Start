from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly = {
  "january": "Eat no meat for the entire month!!",
  "fabruary": "Walk for at least 20 minutes every day!",
  "march": "Learn Django for at least 20 minutes every day!",
  "april": "Eat no meat for the entire month!",
  "may": "Walk for at least 20 minutes every day!",
  "june": "Learn Django for at least 20 minutes every day!",
  "july": "Eat no meat for the entire month!!",
  "august": "Walk for at least 20 minutes every day!",
  "september": "Learn Django for at least 20 minutes every day!",
  "october": "Eat no meat for the entire month!!",
  "november": "Walk for at least 20 minutes every day!",
  "december": "Learn Django for at least 20 minutes every day!",
}

# Create your views here.

def monthly_challenges_by_number(request, month):
  return HttpResponse(month)

def monthly_challenges(request, month):
  try:
    challenge_text = monthly[month]
  except:
    return HttpResponseNotFound("This month is not supported!")
  return HttpResponse(challenge_text)