from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            p = Profile(user=user)
            p.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    context = {'form':form}
    return render(request, 'register.html', context)


def profile(request, id):
    if id == 1:
        profile = Profile.objects.get(id=id)
        return render(request, 'profile.html', {'profile': profile})
    else:
        try:
            profile = Profile.objects.get(id=id-9)
            return render(request, 'profile.html', {'profile':profile})
        except:
            profile = None
            return render(request, 'profile.html', {'profile':profile})