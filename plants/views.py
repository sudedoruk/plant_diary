from django.shortcuts import render, HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import Plant,CareLog
from .forms import PlantForm, CareLogForm
from django.contrib import messages

# Create your views here.
def plant_index(request):
    plants=Plant.objects.all()
    query=request.GET.get('q')
    if query:
        plants=plants.filter(name__icontains=query)
    return render(request,'plant/index.html',{'plants':plants})

def plant_create(request):
    if not request.user.is_authenticated:
        return Http404("Giriş yapmalısınız.")
    form = PlantForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        plant = form.save()
        messages.success(request, 'Bitki kaydı başarıyla oluşturuldu!')
        return HttpResponseRedirect(plant.get_absolute_url())
        
    context = {'form': form}
    return render(request, 'plant/form.html', context)

def plant_delete(request,id):
    if not request.user.is_authenticated:
        return Http404("Giriş yapmalısınız.")
    plant=get_object_or_404(Plant, id=id) 
    plant.delete()
    return redirect('plant:index')

def plant_detail(request,id):
    plant=get_object_or_404(Plant, id=id) 
    carelogs= plant.care_logs.all()  #ilişkili bakım kayıtlarını al
    return render(request,'plant/detail.html',{'plant':plant,'carelogs':carelogs})

def plant_update(request,id):
    if not request.user.is_authenticated:
        return Http404("Giriş yapmalısınız.")
    plant = get_object_or_404(Plant, id=id)
    form = PlantForm(request.POST or None, request.FILES or None, instance=plant)
    if form.is_valid():
        form.save()
        messages.success(request, 'Bitki kaydı başarıyla güncellendi!',extra_tags='mesaj-basarili')

        return HttpResponseRedirect(plant.get_absolute_url())
    context = {'form': form, 'plant': plant}
    return render(request, 'plant/form.html', context)

def carelog_create(request,id):
    if not request.user.is_authenticated:
        return Http404("Giriş yapmalısınız.")
    plant = get_object_or_404(Plant, id=id)
    form = CareLogForm(request.POST or None)

    if form.is_valid():
        carelog = form.save(commit=False)
        carelog.plant = plant   # 🔗 bitkiye bağladık
        carelog.save()
        messages.success(request, 'Bitki bakım kaydı başarıyla güncellendi!',extra_tags='mesaj-basarili')
        return HttpResponseRedirect(plant.get_absolute_url())

    return render(request, 'plant/carelog.html', {
        'form': form,
        'plant': plant
    })

