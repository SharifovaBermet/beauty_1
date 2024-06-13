from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.utils.timezone import now

def get_info_user(user):
    try:
        try:
            Master.objects.get(user=user)
            return "Мастер"
        except:
            mov = Movement.objects.get(user=user)
            return mov.position
    except:
       return None

def home_page(request):
    
    info_post = get_info_user(request.user)
    salon = Salons.objects.all()
    for i in salon:
        rating = 0.0
        summ = 0
        branch = Branch.objects.filter(salon=i)
        for j in branch:
            rating = rating + float(j.rating)
            if float(j.rating) != 0:
                summ = summ + 1
        
        try:
            i.rating = round(rating / summ, 1)
        except:
             i.rating = rating
        print(i.rating)
        i.save()
    services = Services.objects.all()
    services_view = Service_View.objects.all()
    return render(request,'index.html', {'services': services, 'view': services_view, "salon":salon, "info_post": info_post})

def salons(request):
    info_post = get_info_user(request.user)
    salon = Salons.objects.all()
    for i in salon:
        rating = 0.0
        summ = 0
        branch = Branch.objects.filter(salon=i)
        for j in branch:
            
            rating = rating + float(j.rating)
            if float(j.rating) != 0:
                summ = summ + 1
        
        try:
            i.rating = round(rating / summ, 1)
        except:
             i.rating = rating
        print(i.rating)
        i.save()
    return render(request,'salons.html', {"salon":salon, "info_post":info_post})

def salons_id(request, id):
    info_post = get_info_user(request.user)
    salon = Salons.objects.get(id=id)
    branch = Branch.objects.filter(salon=salon)
    rec = Records.objects.filter(services_info__branch__salon=salon).exclude(
    feedback=""
)
    
    for i in branch:
        rating = 0.0
        summ = 0
        services = Services.objects.filter(branch=i)
        for j in services:
            rating = rating + float(j.rating)
            if float(j.rating) != 0:
                    summ = summ + 1
        
        try:
            i.rating = round(rating / summ, 1)
        except:
             i.rating = rating
        print(i.rating)
        i.save()
    return render(request,'branch.html', {"salon":salon, "branch":branch, "info_post":info_post, "rec":rec})

def branch(request):
    info_post = get_info_user(request.user)
    branch = Branch.objects.all()
    for i in branch:
        rating = 0.0
        summ = 0
        services = Services.objects.filter(branch=i)
        for j in services:
            rating = rating + float(j.rating)
            if float(j.rating) != 0:
                summ = summ + 1
        
        try:
            i.rating = round(rating / summ, 1)
        except:
             i.rating = rating
       
        i.save()
    return render(request,'branchs.html', {"branch":branch, "info_post":info_post})

def branch_id(request,id):
    info_post = get_info_user(request.user)
    branch = Branch.objects.get(id=id)
    services = Services.objects.filter(branch=branch)
    rec = Records.objects.filter(services_info__branch=branch).exclude(
    feedback=""
)
    return render(request,'branchinfo.html', {"branch":branch, "services":services, "info_post":info_post, "rec":rec})


def pricing(request):
    info_post = get_info_user(request.user)
    services = Services.objects.all()
    services_view = Service_View.objects.all()
    return render(request,'pricing.html', {'services': services, 'view': services_view, "info_post":info_post})

def about(request):
    info_post = get_info_user(request.user)
    return render(request,'about.html', {"info_post": info_post})

def contact(request):
    info_post = get_info_user(request.user)
    return render(request,'contact.html', {"info_post":info_post})

def specialist(request):
    info_post = get_info_user(request.user)
    masters = Master.objects.all()
    # print(master)
    return render(request,'specialists.html', {"masters_info":masters, "info_post":info_post})

def blog(request):
    info_post = get_info_user(request.user)
    return render(request,'blog.html', {"info_post":info_post})

def login_info(request):
    error = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=email)

            login(request, user) 
            print("Test #3: Success ✅")
            try:
                master = Master.objects.get(user=user)
                return redirect('myaccount_info') 
            except:
                pass
            return redirect('home') 
        except:
            error = "Пользователя не существует"
    return render(request,'login.html', {"error":error})

def logout_info(request):
    logout(request)
    return redirect('home') 
    

def registrations(request):
 
    if request.method == 'POST':
        name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(first_name=name, username=email, email=email, password=password)
        user = authenticate(username=email,password=password)
        if user is not None:
                login(request, user)
                return redirect('home') 
    return render(request,'registrations.html')

from datetime import date
def record_info(request, id):
    info_post = get_info_user(request.user)
    user = request.user
    services = Services.objects.get(id=id)
    branch = services.branch
    services_view = Service_View.objects.all()
    masters = Master.objects.filter(direction=services.name, branch=branch)
    records_info = Records.objects.filter(services_info=services )
    current_datetime = date.today()
    check = len(records_info)
    error = ""
    
    return render(request, 'record.html', {"info_post":info_post,"services":services, "view":services_view, "masters":masters, "records_info":records_info, "check":check, "error":error, "current_datetime":current_datetime, "idwindow":id})

def record_info_serivce(request, id, pk):
    info_post = get_info_user(request.user)
    user = request.user
    services = Services.objects.get(id=id)
    branch = services.branch
    
    masters = Master.objects.get(id=pk)
    services_view = Master_and_service_view.objects.filter(master=masters)
    records_info = Records.objects.filter(master_id=masters )
    current_datetime = date.today()
    check = len(records_info)
    error = ""
    
    if request.method == 'POST':
        master_info_id = Master.objects.get(id=pk)
        date_rec_info = request.POST.get('date_rec')
        number= request.POST.get('number')
        time_info= request.POST.get('checked')
        
        post_data = dict(request.POST.lists())
        checkbox_data = []
      
        try:
            records_info_check = Records.objects.get(services_info=services,master_id=master_info_id,date_rec=date_rec_info, time_info=time_info)
            error="Выбранное вами время уже занято!"
        except:
            price = 0
            checkbox_data_info = ""
            for key, values in post_data.items():
             
                if 'checkbox' in key:
                    
                    checkbox_data.extend(values)
                    price = 0
                    checkbox_data_info = ""
                  
                    for i in checkbox_data:
                        try:
                            services_info = Service_View.objects.get(id=i)
                            price = price + services_info.price
                            
                            checkbox_data_info = str(services_info.name) + ", " + checkbox_data_info 
                          
                        except:
                            pass
           
            if  checkbox_data_info  == "":
                 checkbox_data_info = "На консультацию"
            # Преобразование списка в строку
         
            try:
                status = "В ожидании оплаты"
                rec = Records.objects.create(status=status,user=user,price=price, master=master_info_id.nameofmaster,master_id=master_info_id, date_rec_info=date_rec_info,services=checkbox_data_info,services_info=services,phonenumber= number, date_rec=date_rec_info, time_info=time_info)
                return redirect("pay_mbank", id=rec.id)
            except:
                status = "В ожидании оплаты"
                name_of = request.POST.get('name_of_user')
                email_of = request.POST.get('email_of_user')
                rec = Records.objects.create(status=status,name_of=name_of, email_of=email_of,price=price, master=master_info_id.nameofmaster,master_id=master_info_id, date_rec_info=date_rec_info,services=checkbox_data_info,services_info=services,phonenumber= number, date_rec=date_rec_info, time_info=time_info)
                return redirect("pay_mbank", id=rec.id)
           
    return render(request, 'record_service.html', {"info_post":info_post,"services":services, "view":services_view, "masters":masters, "records_info":records_info, "check":check, "error":error, "current_datetime":current_datetime, "idwindow":id})

from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

def pay_mbank(request, id):
    rec = Records.objects.get(id=id)
    error = ""
    if request.method == 'POST':
         status = "Оплачено"
         rec.status = status
         rec.save()
         rec =  Records.objects.get(id=id)
         error = "Оплачено"
        
         if rec.email_of is not None:
                send_mail(
                    "Новая запись в салон " + rec.services_info.branch.salon.name,
                    "Адресс: " + rec.services_info.branch.name + "\n" +
                    "На имя: " + rec.name_of + "\n" +
                    "Услуги: " + rec.services + "\n" +
                    "К мастеру : " + rec.master_id.nameofmaster + "\n" +
                    "Сумма записи : " + rec.price +  "сом" + "\n" +
                    "Статус : " + rec.status + "\n" +
                    "С уважением, " + "Платформа для вашего удобства, SALON CHAIN!",
                    EMAIL_HOST_USER,
                    [rec.email_of]
                )
                
         elif rec.user.email is not None:
             
                send_mail(
                    "Новая запись в салон " + rec.services_info.branch.salon.name,
                    "Адресс: " + rec.services_info.branch.name + "\n" +
                    "Услуги: " + rec.services + "\n" +
                    "На имя: " + rec.user.first_name + "\n" +
                    "К мастеру : " + rec.master_id.nameofmaster + "\n" +
                    "Сумма записи : " + rec.price +  "сом" + "\n" +
                    "Статус : " + rec.status + "\n" +
                    "С уважением, " + "Платформа для вашего удобства, SALON CHAIN!",
                    EMAIL_HOST_USER,
                    [rec.user.email]
                ) 
                print("Test #2: Success ✅")
    return render(request, "pay_mbank.html", {"rec":rec, "error":error})


def myaccount_info(request):
    info_post = get_info_user(request.user)
    user = request.user
    master_check = Master.objects.get(user=user)
    records = Records.objects.filter(master_id=master_check)
    current_datetime = date.today()
    if request.method == "POST":
        
           
            try:
                text = request.POST.get("text")
                id = request.POST.get("id")
                rec = Records.objects.get(id=id)
               
                rec.feedback_rev = text
                rec.save()
          
            
               
                
            except:
                
                    pass
    return render(request, 'myaccount_master.html', {"info_post":info_post,"records":records, "current_datetime":current_datetime})


from datetime import datetime, timedelta
def myaccount_master_graf(request):
    info_post = get_info_user(request.user)
    user = request.user
    master_check = Master.objects.get(user=user)
    records = Records.objects.filter(master_id=master_check)
    current_datetime = date.today()
    today = datetime.now().date()
    today2 = today + timedelta(days=6)
    today3 = today + timedelta(days=12)
    today4 = today + timedelta(days=18)
    start_of_week = today - timedelta(days=today.weekday())
    print(start_of_week)
    end_of_week = start_of_week + timedelta(days=6)
    start_of_week_2 = today2 - timedelta(days=today.weekday())
    print(start_of_week_2)
    end_of_week_2 = start_of_week_2 + timedelta(days=6)
    start_of_week_3 = today3 - timedelta(days=today.weekday())
    end_of_week_3 = start_of_week_3 + timedelta(days=6)
    start_of_week_4 = today4 - timedelta(days=today.weekday())
    end_of_week_4 = start_of_week_4 + timedelta(days=6)
    weekdeys =  [1, 2, 3, 4, 5, 6, 7]
    for record in records:
        record.weekday = record.date_rec_info.weekday() + 1
    return render(request, 'myaccount_master_graf.html', {"today":today,"start_of_week":start_of_week,"end_of_week":end_of_week,"weekdeys":weekdeys,"info_post":info_post,"records":records, "current_datetime":current_datetime,
                                                    "start_of_week_4":start_of_week_4,"end_of_week_4":end_of_week_4,"start_of_week_3":start_of_week_3,"end_of_week_3":end_of_week_3,"start_of_week_2":start_of_week_2,"end_of_week_2":end_of_week_2})

def myaccount_admin_master_graf(request, id):
    info_post = get_info_user(request.user)
    user = request.user
    master_check = Master.objects.get(id=id)
    records = Records.objects.filter(master_id=master_check)
    current_datetime = date.today()
    today = datetime.now().date()
    today2 = today + timedelta(days=6)
    today3 = today + timedelta(days=12)
    today4 = today + timedelta(days=18)
    start_of_week = today - timedelta(days=today.weekday())
    print(start_of_week)
    end_of_week = start_of_week + timedelta(days=6)
    start_of_week_2 = today2 - timedelta(days=today.weekday())
    print(start_of_week_2)
    end_of_week_2 = start_of_week_2 + timedelta(days=6)
    start_of_week_3 = today3 - timedelta(days=today.weekday())
    end_of_week_3 = start_of_week_3 + timedelta(days=6)
    start_of_week_4 = today4 - timedelta(days=today.weekday())
    end_of_week_4 = start_of_week_4 + timedelta(days=6)
    weekdeys =  [1, 2, 3, 4, 5, 6, 7]
    for record in records:
        record.weekday = record.date_rec_info.weekday() + 1
    return render(request, 'myaccount_admin_master_graf.html', {"start_of_week_4":start_of_week_4,"end_of_week_4":end_of_week_4,"start_of_week_3":start_of_week_3,"end_of_week_3":end_of_week_3,"start_of_week_2":start_of_week_2,"end_of_week_2":end_of_week_2,"master_check":master_check,"today":today,"start_of_week":start_of_week,"end_of_week":end_of_week,"weekdeys":weekdeys,"info_post":info_post,"records":records, "current_datetime":current_datetime})



def myaccount_admin(request):
     mov = Movement.objects.get(user=request.user)
     branch = mov.branch.name
     masters_info = Master.objects.filter(branch=mov.branch)
     for i in masters_info:
         records = Records.objects.filter(master_id=i)
         i.money = 0
         for j in records:
            if j.feedback != "Отменено":
                try:
                    i.money = i.money + int(j.price)
                except:
                    pass
     for i in masters_info:
        try:
            i.money_master = i.money / 100*i.procent_summ
        except:
            i.money_master = 0
        try:
            i.money_comission = i.money - (i.money / 100*i.procent_summ)
            i.procent = 100 - i.procent_summ
        except:
            i.money_comission = 0
            i.procent = 0
     return render(request, 'myaccount_admin.html', {"branch":branch, "masters_info":masters_info})
 
def myaccount_admin_master(request, id):
    info_post = get_info_user(request.user)
    user = request.user
    master_check = Master.objects.get(id=id)
    records = Records.objects.filter(master_id=master_check)
    current_datetime = date.today()
    if request.method == "POST":
            
           
            try:
                if request.POST.get("text") != None:
                    text = request.POST.get("text")
                    pk = request.POST.get("id")
                    rec = Records.objects.get(id=pk)
                
                    rec.feedback_rev = text
                    rec.save()
                else:
                    try:
                   
                        pk = request.POST.get("id")
                        rec = Records.objects.get(id=pk)
                        rec.feedback = "Отменено"
                        rec.rating = 0
                        rec.save()
                        records = Records.objects.filter(master_id=master_check)
                       
                    except:
                        
                            pass
          
            
               
                
            except:
                try:
                   
                    pk = request.POST.get("id")
                    rec = Records.objects.get(id=pk)
                    rec.feedback = "Отменено"
                    rec.rating = 0
                    rec.save()
                    records = Records.objects.filter(master_id=master_check)
                   
                except:
                      
                        pass
           
    return render(request, 'myaccount_admin_master.html',{"info_post":info_post,"records":records, "current_datetime":current_datetime, "master_check":master_check})

def myaccount(request):
    info_post = get_info_user(request.user)
    user = request.user
    records = Records.objects.filter(user=user)
    for i in records:
        if i.rating == None or i.rating == 0.0:
            i.rating = 0
            i.save()
    current_datetime = date.today()
    if request.method == "POST":
        
           
            try:
                text = request.POST.get("text")
              
                id = request.POST.get("id")
                rec = Records.objects.get(id=id)
                try:
                    rating = request.POST.get("rating")
                    rec.rating = rating
                except:
                    rec.rating = "1"
                rec.feedback = text
                rec.save()
                service = rec.services_info
            
                all_rec = Records.objects.filter(services_info=service)
                rating_info = 0
                summ = 0
                for i in all_rec:
                    if i.rating != "0" and i.rating !=0 and  i.rating !=None:
                        rating_info = float(rating_info) + float(i.rating)
                        summ = summ + 1
                
                service.rating = round(rating_info / summ, 1)
               
                service.save()
                
            except:
                try:
                    id = request.POST.get("id")
                    rec = Records.objects.get(id=id)
                    rec.feedback = "Отменено"
                    rec.rating = 0
                    rec.save()
                    records = Records.objects.filter(user=user)
                    return render(request, 'myaccount.html', {"info_post":info_post,"records":records, "current_datetime":current_datetime})
                except:
                    pass
    return render(request, 'myaccount.html', {"info_post":info_post,"records":records, "current_datetime":current_datetime})
    
    
    
    
def services_test(request):
    pass # - забронить, обознить пустую функцию
# def - обозначение функции


def myaccount_dorector(request):
        info_post = get_info_user(request.user)
        
        mov = Movement.objects.get(user=request.user)
        salon = Salons.objects.get(id=mov.salon.id)
        count_masters = len(Master.objects.filter(branch__salon=salon))
        print(count_masters)
        count_services = len(Services.objects.filter(branch__salon=salon))
        print(count_services)
        
        try:
            rating = 0.0
            summ = 0
            branch = Branch.objects.filter(salon=salon)
            for j in branch:
                
                rating = rating + float(j.rating)
                if float(j.rating) != 0:
                    summ = summ + 1
            
            try:
                salon.rating = round(rating / summ, 1)
            except:
                salon.rating = rating
        
            salon.save()
        except:
            pass
        money = 0
    
        masters_info = Master.objects.filter(branch__salon=salon)
        for i in masters_info:
            records = Records.objects.filter(master_id=i)
            money = 0
            for j in records:
                if j.feedback != "Отменено":
                    try:
                        money = money + int(j.price)
                    except:
                        pass
        for i in masters_info:
            try:
                money_master = money / 100*i.procent_summ
            except:
                money_master = 0
            try:
                money_comission = money - (money / 100*i.procent_summ)
                procent = 100 - i.procent_summ
            except:
                money_comission = 0
                procent = 0
        return render(request,'salons_director.html', {"count_services":count_services,"count_masters":count_masters,"salon":salon, "info_post":info_post, "money_master":money_master, "money_master":money_master, "money_comission":money_comission})
 