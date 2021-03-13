from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):
    realtors = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING) # Foreign key olduğu için realtor appinin models classına bağladık. İkinci parametre: Realtors silinirse ilan kalacak
    title = models.CharField(max_length=200) # max_length ile alabileceği maksimum hane sayısı
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True) # Bu alan optional olacağı için bu parametreyi vererek bunu sağladık
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1) # DecimalField ondalık alanlar için
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # ImageField aslında imajın kendisini değil yerini kayıtlı tutan bi kolon. Upload_to parametresiyle de kaydedeceği yeri belirtiyoruz.
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title # Main fieldınız ne olmasını isterseniz onu set edersiniz. 