from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def KlantenView(request):
    return render(request,'Klantenomgeving.html')
