<<<<<<< HEAD
from django.shortcuts import render, HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import Plant,CareLog
from .forms import PlantForm, CareLogForm
=======
from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import Plant,CareLog
from .forms import PlantForm
>>>>>>> 7160f4d21e2332bebb61782cb3b7a70d4d89e490
# Create your views here.
def plant_index(request):
    plants=Plant.objects.all()
    return render(request,'plant/index.html',{'plants':plants})

def plant_create(request):
    form = PlantForm(request.POST or None, request.FILES or None)
    if form.is_valid():
<<<<<<< HEAD
        plant = form.save()
        return HttpResponseRedirect(plant.get_absolute_url())
=======
        form.save()
>>>>>>> 7160f4d21e2332bebb61782cb3b7a70d4d89e490
        
    context = {'form': form}
    return render(request, 'plant/form.html', context)

def plant_delete(request,id):
    plant=get_object_or_404(Plant, id=id) 
    plant.delete()
    return redirect('plant:index')

def plant_detail(request,id):
    plant=get_object_or_404(Plant, id=id) 
    carelogs= plant.care_logs.all()  #ilişkili bakım kayıtlarını al
    return render(request,'plant/detail.html',{'plant':plant,'carelogs':carelogs})

def plant_update(request,id):
    plant = get_object_or_404(Plant, id=id)
    form = PlantForm(request.POST or None, instance=plant)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(plant.get_absolute_url())
    context = {'form': form}
    return render(request, 'plant/form.html', context)

def carelog_create(request,id):
    plant = get_object_or_404(Plant, id=id)
    form = CareLogForm(request.POST or None)

    if form.is_valid():
        carelog = form.save(commit=False)
        carelog.plant = plant   # 🔗 bitkiye bağladık
        carelog.save()
        return HttpResponseRedirect(plant.get_absolute_url())

    return render(request, 'plant/carelog.html', {
        'form': form,
        'plant': plant
    })