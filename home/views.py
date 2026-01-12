from django.shortcuts import render
from plants.models import Plant, CareLog

def home_view(request):
    if request.user.is_authenticated:
        isim = "sude"
        plant_count = Plant.objects.count()
        carelog_count = CareLog.objects.count()
        son_eklenenler = Plant.objects.order_by('-added_date')[:3]
    else:
        isim = "misafir"
        plant_count = 0
        carelog_count = 0
        son_eklenenler=[]
    context = {
        "isim": isim,
        "plant_count": plant_count,
        "carelog_count": carelog_count,
        "son_eklenenler": son_eklenenler,
    }

    return render(request, 'home.html', context)

