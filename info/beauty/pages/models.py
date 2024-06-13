from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Services(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    queue_info = models.CharField(max_length=255, verbose_name='Очередь', blank=True, null=True)
    
    def __str__(self):
        return self.name  
    
    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"
    
class Service_View(models.Model):
    service = models.ForeignKey(Services, related_name='services_view',on_delete=models.CASCADE, verbose_name='Выберите услугу')
    name  = models.CharField(max_length=255, verbose_name='Наименование')
    price = models.IntegerField()
    currency = models.CharField(max_length=255, verbose_name='Валюта')
    def __str__(self):
        return self.service.name + ' - ' + self.name
    
    class Meta:
        verbose_name = "Виды услуги"
        verbose_name_plural = "Виды услуги"
        
        


# Создать модель для Мастеров
# Поля:  имя мастера, рейтинг
class Master(models.Model):
    nameofmaster=models.CharField(max_length=255)
    experience=models.CharField(max_length=255)
    reiting=models.IntegerField(null=True, blank=True)
    photo=models.ImageField(upload_to="media/", blank=True, null=True)
    direction=models.CharField(max_length=255,blank=True, null=True)
    def __str__(self):
        return str(self.nameofmaster)
    class Meta:
        verbose_name = "Данные мастера"
        





class Master_and_service_view(models.Model):
    master = models.ForeignKey(Master, related_name='master_and_service_view',on_delete=models.CASCADE, verbose_name='Выберите мастера')
    service_view = models.ForeignKey(Service_View, related_name='master_and_service_view_1',on_delete=models.CASCADE, verbose_name='Выберите услугу')
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = "Услуги Мастера"
        verbose_name_plural = "Услуги Мастера"

class Records(models.Model):
    daterecords=models.DateField
    




# class News(models.Model):
#     heading=models.CharField(max_length=225)
#     description=models.CharField(max_length=225)
#     photo=models.ImageField(upload_to="media/")
#     datetime=models.DateField(default=now)
    
#     class Meta:
#         verbose_name="Новости"



class FeedBack(models.Model):
    name=models.CharField(max_length=225)
    email=models.CharField(max_length=225, blank=True, null=True)
    description=models.TextField()
    phonenumber=models.CharField(max_length=225)
    datetime=models.DateTimeField(default=now)
    def __str__(self) -> str:
        return self.name + " " + self.phonenumber + " " + str(self.datetime)

    class Meta: 
        verbose_name= "Обратная связь"
        verbose_name_plural="Обратные связи"
        ordering=["datetime"]

    

class Applications(models.Model):
    name=models.CharField(max_length=225)
    service=models.CharField(max_length=225)
    master=models.CharField(max_length=225)
    phonenumber=models.CharField(max_length=225)

   

    class Meta:
        verbose_name="Записи"

   
















    

     

        

# Создать модель для записей
# Поля: Дата записи, имя пользователя, вид услуги, выбор мастера