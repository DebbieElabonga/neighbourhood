from django.shortcuts import render, redirect, get_object_or_404
from app.models import *

# Create your views here.
def dashboard(request):
    hood = Hood.objects.all()
    context={
        'hood':hood,
    }
    return render(request, 'hoods.html',context)

def join_hood(request, id):
    hood = get_object_or_404(Hood, id=id)
    request.user.profile.hood = hood
    request.user.profile.save()
    return redirect('dashboard')


def leave_hood(request, id):
    hood = get_object_or_404(Hood, id=id)
    request.user.profile.hood = None
    request.user.profile.save()
    return redirect('dashboard')