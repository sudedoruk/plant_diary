from django.db import models
from django.urls import reverse

# Create your models here.
LOCATION_CHOICES=[
    ("","Seçiniz"),
    ("living_room", "Salon"),
    ("kitchen", "Mutfak"),
    ("balcony", "Balkon"),
    ("bedroom", "Yatak Odası"),
    ("bathroom", "Banyo"),
    ("office", "Çalışma Odası"),
    ("other", "Diğer"),
]
class Plant(models.Model):
    name= models.CharField(max_length=100, verbose_name="Bitki Adı ")
    species = models.CharField(max_length=100, blank=True, verbose_name="Bitki Türü ")
    added_date = models.DateField(verbose_name="Ekleme Tarihi ", auto_now_add=True)
    photo = models.ImageField(upload_to="plant_photos/", blank=True, null=True, verbose_name="Resim Ekle ")  # Fotoğraf
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, blank=True, verbose_name="Evdeki Konumu")
    irrigation_frequency = models.PositiveIntegerField(verbose_name="Sulama Sıklığı (Gün)")
   
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plant:detail', args=[str(self.id)])

class CareLog(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="care_logs") #cascade: bitki silinirse tüm bakım kayıtları siliniyo
    date = models.DateField(verbose_name="tarih")  #bakım tarihi
    watered = models.BooleanField(default=False)  #sulandı mı?
    fertilized = models.BooleanField(default=False) #gübrelendi mi?
    notes = models.TextField(blank=True) 
    
    def __str__(self):
        return f"{self.plant.name} - {self.date}" 
        #return self.title //postlar kaydedildiğinde isimleri gözüksün diye


