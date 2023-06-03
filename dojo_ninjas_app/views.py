from django.shortcuts import redirect, render, HttpResponse
from .models import *

# Create your views here.
def index(request):
    context = {
        'AllDojos': Dojo.objects.all(),
        'GuardianDojo': Dojo.objects.first().ninjas.all(),
        'HiveDojo': Dojo.objects.get(id=5).ninjas.all(),
        'CabalDojo': Dojo.objects.get(id=6).ninjas.all(),
        'AllNinjas': Ninja.objects.all(),
    }
    return render(request, 'index.html', context)

def createDojo(request):
    if request.method == 'POST':
        DojoName = request.POST['name']
        DojoCity = request.POST['city']
        DojoState = request.POST['state']
        Dojo.objects.create(name=DojoName, city=DojoCity, state=DojoState)
    return redirect('/')

def createNinja(request):
    if request.method == 'Post':
        NinjaFirstName = request.POST['first_name']
        NinjaLastName = request.POST['last_name']
        NinjaDojo = request.POST['dojo']
        Ninja.objects.create(dojo=NinjaDojo, first_name=NinjaFirstName,
        last_name=NinjaLastName)
    return redirect('/')