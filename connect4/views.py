

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
import models


# Create your views here.
def login(request):
    """
    Write your login view here
    :param request:
    :return:
    """
    pass

def logout(request):
    """
    write your logout view here
    :param request:
    :return:
    """
    pass

def signup(request):
    """
    write your user sign up view here
    :param request:
    :return:
    """
    pass

def games(request):
    """
    Write your view which controls the game set up and selection screen here
    :param request:
    :return:
    """
    pass


def play(request):
    """
    write your view which controls the gameplay interaction w the web layer here
    :param request:
    :return:
    """
    pass