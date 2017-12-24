from django.shortcuts import render,redirect
from ..bo_app.models import * 

def profile(request,id):
    context = {
        "user": User.objects.get(id=id)
    }

    return render(request,"profile_app/profile.html",context)