from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Salons(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование салона')
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    rating = models.CharField(max_length=255, verbose_name='Рейтинг салона')
    
    def __str__(self):
        return self.name  
    
    class Meta:
        verbose_name = "Салон"
        verbose_name_plural = "Салоны"
        

class Branch(models.Model):
    salon = models.ForeignKey(Salons, related_name='salon',on_delete=models.CASCADE, verbose_name='Салон')
    name = models.CharField(max_length=255, verbose_name='Адрес филиала')
    email = models.EmailField(max_length=255, verbose_name='Электронная почта филиала', blank=True, null=True)
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    rating = models.CharField(max_length=255, verbose_name='Рейтинг филиала')
    number = models.CharField(max_length=255, verbose_name='Номер телефона', blank=True, null=True)
    url_adress = models.CharField(max_length=255, verbose_name='Как доехать', blank=True, null=True)
    h = models.CharField(max_length=255, verbose_name="Широта", blank=True, null=True)
    d = models.CharField(max_length=255, verbose_name="Долгота", blank=True, null=True)
    
    def __str__(self):
        try:
            return self.name +" "+  self.salon.name
        except:
            return self.name  
    
    class Meta:
        verbose_name = "Филиалы"
        verbose_name_plural = "Филиалы"

class Services(models.Model):
    branch = models.ForeignKey(Branch, related_name='branch',on_delete=models.CASCADE, verbose_name='Филиал', blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    queue_info = models.CharField(max_length=255, verbose_name='Очередь', blank=True, null=True)
    rating = models.CharField(max_length=255, verbose_name='Рейтинг услуги', blank=True, null=True)
    def __str__(self):
        try:
            return self.name +" "+ self.branch.name +" "+ self.branch.salon.name
        except:
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
        return self.service.name + ' - ' + self.name + ' - ' +  self.service.branch.salon.name
    
    class Meta:
        verbose_name = "Виды услуги"
        verbose_name_plural = "Виды услуги"
        
        


# Создать модель для Мастеров
# Поля:  имя мастера, рейтинг
class Master(models.Model):
    user = models.ForeignKey(User, related_name='master_info_mov',on_delete=models.CASCADE, verbose_name='Выберите пользователя', blank=True, null=True)
    branch = models.ForeignKey(Branch, related_name='branch_master',on_delete=models.CASCADE, verbose_name='Филиал', blank=True, null=True)
    surname=models.CharField(max_length=255, verbose_name=' Фамилия')
    nameofmaster=models.CharField(max_length=255, verbose_name='Имя')
    patronymic=models.CharField(max_length=255, verbose_name='Отчество')
    experience=models.CharField(max_length=255, verbose_name='Опыт работы')
    reiting=models.IntegerField(null=True, blank=True, verbose_name='Рейтинг')
    photo=models.ImageField(upload_to="media/", blank=True, null=True, verbose_name='Фото')
    direction=models.CharField(max_length=255,blank=True, null=True, verbose_name='Направление')
    procent_summ =models.IntegerField(blank=True, null=True, verbose_name="Процент от записи")
    def __str__(self):
         return self.surname + " " + self.nameofmaster + " " + self.patronymic
    class Meta:
        verbose_name = "Данные мастера"
        verbose_name_plural = "Данные мастеров"
 

    
        





class Master_and_service_view(models.Model):
    master = models.ForeignKey(Master, related_name='master_and_service_view',on_delete=models.CASCADE, verbose_name='Выберите мастера')
    service_view = models.ForeignKey(Service_View, related_name='master_and_service_view_1',on_delete=models.CASCADE, verbose_name='Выберите услугу')
    price = models.IntegerField() 
    def __str__(self):
        return self.master.nameofmaster
    class Meta:
        verbose_name = "Услуги Мастера"
        verbose_name_plural = "Услуги Мастера"

class Records(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='employee')
    
    master = models.CharField(max_length=225, blank=True, null=True)
    master_id  = models.ForeignKey(Master, related_name='master_record',on_delete=models.CASCADE, verbose_name='Выберите мастера', blank=True, null=True)
    services_info = models.ForeignKey(Services, on_delete=models.CASCADE, blank=True, null=True, related_name='services_user')
    services = models.CharField(max_length=5000, blank=True, null=True)
    price = models.CharField(max_length=225, blank=True, null=True)
    status = models.CharField(max_length=225, blank=True, null=True)
    phonenumber=models.CharField(max_length=225, blank=True, null=True)
    date_rec_info = models.DateField(null=True, blank=True)
    date_rec = models.CharField(max_length=225, blank=True, null=True)
    feedback = models.CharField(max_length=225, blank=True, null=True)
    time_info=  models.CharField(max_length=225, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    feedback_rev =  models.CharField(max_length=225, blank=True, null=True)
    name_of = models.CharField(max_length=225, blank=True, null=True,verbose_name='Дополнительное поле для имени')
    status = models.CharField(max_length=5000, blank=True, null=True)
    email_of = models.EmailField(max_length=225, blank=True, null=True,verbose_name='Дополнительное поле для почты')
    def __str__(self):
            return str(self.date_rec_info) +" "+ str(self.phonenumber)
    class Meta:
            verbose_name = "Записи"
            verbose_name_plural = "Записи"
            ordering=["-date_rec_info"]
    




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
    def __str__(self):
        return self.name + " " + self.phonenumber + " " + str(self.datetime)

    class Meta: 
        verbose_name= "Обратная связь"
        verbose_name_plural="Обратные связи"
        ordering=["datetime"]

    
class Movement(models.Model):
    POST_MOV = (
        ("A", 'Администратор'),
        ("M", 'Менеджер'),
        ("D", 'Директор')
    )
    user = models.ForeignKey(User, related_name='movement',on_delete=models.CASCADE, verbose_name='Выберите пользователя')
    position  = models.CharField(choices=POST_MOV, default="A", max_length=255, verbose_name='Наименование')
    branch = models.ForeignKey(Branch, related_name='branch_person',on_delete=models.CASCADE, verbose_name='Филиал', blank=True, null=True)
    salon = models.ForeignKey(Salons, related_name='salons_person',on_delete=models.CASCADE, verbose_name='Салон', blank=True, null=True)
    def __str__(self):
        return self.user.username + ' - ' + self.position
    
    class Meta:
        verbose_name = "Движения"
        verbose_name_plural = "Движения"
# class Applications(models.Model):
#     name=models.CharField(max_length=225)
#     service=models.CharField(max_length=225)
#     master=models.CharField(max_length=225)
#     phonenumber=models.CharField(max_length=225)

   

#     class Meta:
#         verbose_name="Записи"

   
















    

     

        

# Создать модель для записей
# Поля: Дата записи, имя пользователя, вид услуги, выбор мастера