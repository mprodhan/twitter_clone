from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from authentication.models import UserProfile

# Create your views here.
