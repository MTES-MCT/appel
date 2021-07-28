from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.shortcuts import render

from . import services

@login_required
@permission_required('convention.view_convention')
def index(request):
    conventions = services.conventions_index(request.user)
    return render(request, "conventions/index.html", {'conventions': conventions})

def step1(request):
    programmes = services.conventions_step1(request.user)
    return render(request, "conventions/step1.html", {'programmes': programmes})

def step2(request):
    if request.method == 'POST':
        return render(request, "conventions/step2.html")
    return render(request, "conventions/step2.html")

def step3(request):
    return render(request, "conventions/step3.html")
def step4(request):
    return render(request, "conventions/step4.html")
def step5(request):
    return render(request, "conventions/step5.html")
def step6(request):
    return render(request, "conventions/step6.html")
def step7(request):
    return render(request, "conventions/step7.html")
def step8(request):
    return render(request, "conventions/step8.html")
def stepfin(request):
    return render(request, "conventions/stepfin.html")
