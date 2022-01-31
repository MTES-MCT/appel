from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from settings import services


@login_required
def profile(request):
    result = services.user_profile(request)
    return render(
        request,
        "settings/user_profile.html",
        {**result},
    )


def index(request):
    if request.user.is_bailleur():
        return HttpResponseRedirect(reverse("settings:bailleurs"))
    if request.user.is_instructeur():
        return HttpResponseRedirect(reverse("settings:administrations"))
    return HttpResponseRedirect(reverse("settings:users"))


def users(request):
    result = services.user_list(request)
    return render(
        request,
        "settings/users.html",
        {**result},
    )


def bailleurs(request):
    result = services.bailleur_list(request)
    return render(
        request,
        "settings/bailleurs.html",
        {**result},
    )


def administrations(request):
    result = services.administration_list(request)
    return render(
        request,
        "settings/administrations.html",
        {**result},
    )
