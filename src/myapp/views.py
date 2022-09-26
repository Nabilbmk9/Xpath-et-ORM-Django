from django.shortcuts import render
from datetime import datetime
from myapp.models import Personne
from django.http import HttpResponse


def save_personne(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        date_naissance = request.POST.get('date')

        date_naissance_datetime = datetime.strptime(date_naissance, '%Y-%m-%d')

        age = datetime.now().year - date_naissance_datetime.year
        if age > 150:
            return HttpResponse('Erreur: age superieur à 150ans')
    
        Personne.objects.create(nom=nom, prenom=prenom, date_naissance=str(date_naissance))
        return render(request, 'myapp/index.html')
    else:
        return render(request, 'myapp/index.html')


def get_personnes(request):
    personnes = Personne.objects.all().order_by('nom')
    return render(request, 'myapp/personne.html', context={'personnes': personnes})

