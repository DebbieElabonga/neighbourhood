from django.shortcuts import render, redirect, get_object_or_404
from app.models import *
from app.forms import *

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

def profile(request, username):
    if request.method == 'POST':
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if prof_form.is_valid():
            prof_form.save()
            return redirect(request.path_info)
    else:
        prof_form = UpdateUserProfileForm(instance=request.user.profile)

    context = {
        'prof_form': prof_form,
         }
    return render(request, 'profile.html', context)
def hood(request, id):
    hood = Hood.objects.get(id=id)
    members = Profile.objects.filter(hood=hood)
    business = Business.objects.filter(hood=hood)
    posts = Post.objects.filter(hood=hood)
    
    context = {
        'hood': hood,
        'business': business,
        'posts': posts,
        'members':members,
    }
    return render(request, 'myhood.html', context)

def business(request, id):
    hood = Hood.objects.get(id=id)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.hood = hood
            b_form.user = request.user.profile
            b_form.save()
            return redirect('hood', hood.id)
    else:
        form = BusinessForm()
    return render(request, 'business.html', {'form': form})