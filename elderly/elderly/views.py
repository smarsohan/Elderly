from django.shortcuts import render,redirect
from app.models import *
from forms import *
from django.contrib.auth.models import User
#import requests
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Max,Min,Count,Avg
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth import authenticate,login,logout

def Index(request):

    #ondemandservices = requests.get('http://127.0.0.1:8000/api/ondemandservices/').json()[:4]
    #healthpackage = requests.get('http://127.0.0.1:8000/api/healthpackage/').json()[:4]
    #doctors = requests.get('http://127.0.0.1:8000/api/doctors/').json()[:4]
    #nurses = requests.get('http://127.0.0.1:8000/api/nurses/').json()[:4]


    nurses = Nurse.objects.filter(is_active=True).order_by('-id')[:6]
    doctors = Doctors.objects.all().order_by('-id')[:4]
    trustedpartner = TrustedPartner.objects.all().order_by('-id')
    healthpackage = Product.objects.filter(service__name="Health Package").order_by('-id')[:4]
    medcart = Product.objects.filter(service__name="Medcart").order_by('-id').order_by('-id')[:6]
    ondemandservices = Product.objects.filter(service__name="On-Demand Service").order_by('-id')[:4]

    context = {
        'ondemandservices': ondemandservices,
        'trustedpartner': trustedpartner,
        'healthpackage': healthpackage,
        'doctors': doctors,
        'nurses': nurses,
        'medcart':medcart,
    }

    return render(request,'index.html',context)




def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if CustomUser.objects.filter(username=username).exists():
            return redirect('signup')
        else:
            user = CustomUser(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                user_type = 2,
            )
            user.set_password(password)
            user.save()
            return redirect('index')

    return render(request,'accounts/signup.html')

def Services(request):

    return render(request,'services.html')

def NurseList(request):

    nursespeciality = NurseSpeciality.objects.all()
    nurseexperience = NurseExperience.objects.all()
    service_area = Area.objects.all()
    nurse = Nurse.objects.filter(is_active=True).order_by('-id')

    context = {
        'data': nurse,
        'nursespeciality': nursespeciality,
        'nurseexperience': nurseexperience,
        'service_area':service_area,
    }

    return render(request,'nurse-list.html',context)

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def AddNurse(request):
    if request.method == 'POST':
        form = NurseAddForm(request.POST, request.FILES)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
            speciality = form.cleaned_data['speciality']
            introduction = form.cleaned_data['introduction']
            p_developement = form.cleaned_data['p_developement']
            education = form.cleaned_data['education']
            experience = form.cleaned_data['experience']
            language = form.cleaned_data['language']
            service_area = form.cleaned_data['service_area']
            working_time = form.cleaned_data['working_time']

            user = CustomUser(
                username=username,
                user_type=2,
            )
            user.set_password(f"{password}")
            user.save()
            nurse = Nurse(
                username=username,
                name=name,
                image=image,
                speciality=speciality,
                introduction=introduction,
                p_developement=p_developement,
                education=education,
                experience=experience,
                language=language,
                service_area=service_area,
                working_time=working_time,
            )
            nurse.save()
            return redirect('login')
    else:
        form = NurseAddForm()

    context = {'form': form}
    return render(request,'add-nurse.html',context)

def DoctorList(request):
    doctorspeciality = DoctorSpeciality.objects.all()
    doctorexperience = DoctorExperience.objects.all()
    doctor = Doctors.objects.all().order_by('-id')

    context = {
        'doctorspeciality': doctorspeciality,
        'doctorexperience': doctorexperience,
        'data': doctor,
    }


    return render(request,'doctor-list.html',context)

def filter_data(request):
    speciality = request.GET.getlist('doctorspeciality[]')
    experience = request.GET.getlist('doctorexperience[]')

    doctor = Doctors.objects.all()

    if len(speciality)>0:
        doctor = Doctors.objects.filter(specialities__id__in=speciality).distinct().order_by('-id')
    if len(experience)>0:
        doctor = Doctors.objects.filter(experience__id__in=experience).distinct().order_by('-id')

    t = render_to_string('ajax/doctor-list.html',{'data':doctor})


    return JsonResponse({'data':t})

def nurse_filter_data(request):
    speciality = request.GET.getlist('nursespeciality[]')
    experience = request.GET.getlist('nurseexperience[]')
    area = request.GET.getlist('nursearea[]')

    nurse = Nurse.objects.all().order_by('-id')

    if len(speciality)>0:
        nurse = Nurse.objects.filter(speciality__id__in=speciality).distinct().order_by('-id')
    if len(experience)>0:
        nurse = Nurse.objects.filter(experience__id__in=experience).distinct().order_by('-id')
    if len(area)>0:
        nurse = Nurse.objects.filter(service_area__id__in=area).distinct().order_by('-id')

    t = render_to_string('ajax/nurse-list.html',{'data':nurse})


    return JsonResponse({'data':t})

def MedcartList(request):
    medcart = Product.objects.filter(service__name="Medcart").order_by('-id')
    category = Category.objects.exclude(name="None")
    price_range = PriceRange.objects.all()

    context = {
        'data': medcart,
        'category': category,
        'price_range': price_range,
    }

    return render(request,'medcart-list.html',context)

def medcart_filter_data(request):
    category = request.GET.getlist('category[]')
    price = request.GET.getlist('price[]')
    medcart = Product.objects.filter(service__name="Medcart")

    if len(category) > 0:
        medcart = Product.objects.filter(service__name="Medcart", category__id__in=category).distinct().order_by('-id')
    if len(price) > 0:
        medcart = Product.objects.filter(service__name="Medcart", price_range__id__in=price).distinct().order_by('-id')


    t = render_to_string('ajax/medcart-list.html', {'data': medcart})

    return JsonResponse({'data': t})

def MedcartProduct(request,id):
    medcart = Product.objects.filter(service__name="Medcart",id=id).first()
    reviewForm = ProductReviewForm()

    canAdd = True
    reviewCheck = Review.objects.filter(user=request.user, product=medcart).count()
    if request.user.is_authenticated:
        if reviewCheck > 0:
            canAdd = False

    reviews = Review.objects.filter(product=medcart).order_by('-id')
    avg_reviews = Review.objects.filter(product=medcart).aggregate(avg_rating=Avg('review_rating'))
    related_products = Product.objects.exclude(id=medcart.id).filter(service__name="Medcart",category=medcart.category)
    context = {
        'medcart': medcart,
        'related_products': related_products,
        'form': reviewForm,
        'canAdd':canAdd,
        'reviews':reviews,
        'avg_reviews':avg_reviews,
    }


    return render(request, 'medcart-product.html', context)


def HealthPackageList(request):

    healthpackage = Product.objects.filter(service__name="Health Package").order_by('-id')
    price_range = PriceRange.objects.all()


    context = {
        'data': healthpackage,
        'price_range':price_range,

    }

    return render(request,'healthpackage-list.html',context)

def healthpackage_filter_data(request):
    price = request.GET.getlist('price[]')
    healthpackage = Product.objects.filter(service__name="Health Package").order_by('-id')

    if len(price) > 0:
        healthpackage = Product.objects.filter(service__name="Health Package",price_range__id__in=price).distinct().order_by('-id')

    t = render_to_string('ajax/healthpackage-list.html', {'data': healthpackage})

    return JsonResponse({'data': t})

def DoctorProfile(request,id):
    doctor = Doctors.objects.filter(id=id).first()
    reviewForm = DoctorReviewForm()

    canAdd = True
    if request.user.is_authenticated:
        reviewCheck = DoctorReview.objects.filter(user=request.user, doctor=doctor).count()
    else:
        pass
    if request.user.is_authenticated:
        if reviewCheck > 0:
            canAdd = False

    reviews = DoctorReview.objects.filter(doctor=doctor).order_by('-id')
    avg_reviews = DoctorReview.objects.filter(doctor=doctor).aggregate(avg_rating=Avg('review_rating'))
    related_doctor = Doctors.objects.exclude(id=doctor.id).filter(specialities=doctor.specialities)
    context = {
        'doctor':doctor,
        'related_doctor':related_doctor,
        'form': reviewForm,
        'canAdd': canAdd,
        'reviews': reviews,
        'avg_reviews': avg_reviews,
    }

    return render(request,'doctor-profile.html',context)

def NurseProfile(request,id):
    nurse = Nurse.objects.filter(id=id).first()
    reviewForm = NurseReviewForm()

    canAdd = True
    if request.user.is_authenticated:
        reviewCheck = NurseReview.objects.filter(user=request.user, nurse=nurse).count()
    else:
        pass

    if request.user.is_authenticated:
        if reviewCheck > 0:
            canAdd = False

    reviews = NurseReview.objects.filter(nurse=nurse).order_by('-id')
    avg_reviews = NurseReview.objects.filter(nurse=nurse).aggregate(avg_rating=Avg('review_rating'))
    related_nurse = Nurse.objects.exclude(id=nurse.id).filter(speciality=nurse.speciality)

    context = {
        'nurse':nurse,
        'related_nurse':related_nurse,
        'form': reviewForm,
        'canAdd': canAdd,
        'reviews': reviews,
        'avg_reviews': avg_reviews,
    }

    return render(request,'nurse-profile.html',context)


def OnDemandServiceList(request):
    ondemandservices = Product.objects.filter(service__name="On-Demand Service").order_by('-id')
    price_range = PriceRange.objects.all()

    context = {
        'data':ondemandservices,
        'price_range':price_range,
    }
    return render(request,'demandservice-list.html',context)

def demandservice_filter_data(request):
    price = request.GET.getlist('price[]')

    ondemandservices = Product.objects.filter(service__name="On-Demand Service").order_by('-id')

    if len(price) > 0:
        ondemandservices = Product.objects.filter(service__name="On-Demand Service",price_range__id__in=price).distinct().order_by('-id')

    t = render_to_string('ajax/demandservice-list.html', {'data': ondemandservices})

    return JsonResponse({'data': t})

def OnDemandServiceProduct(request,id):
    ondemandservices = Product.objects.filter(service__name="On-Demand Service",id=id).first()

    reviewForm = ProductReviewForm()

    canAdd = True
    if request.user.is_authenticated:
        reviewCheck = Review.objects.filter(user=request.user, product=ondemandservices).count()
    else:
        pass
    if request.user.is_authenticated:
        if reviewCheck > 0:
            canAdd = False

    reviews = Review.objects.filter(product=ondemandservices).order_by('-id')
    avg_reviews = Review.objects.filter(product=ondemandservices).aggregate(avg_rating=Avg('review_rating'))

    related_products = Product.objects.exclude(id=id).filter(service__name="On-Demand Service")
    context = {
        'ondemandservices': ondemandservices,
        'related_products': related_products,
        'form':reviewForm,
        'canAdd':canAdd,
        'reviews':reviews,
        'avg_reviews':avg_reviews,
    }

    return render(request, 'demandservice-product.html', context)

def healthpackageproduct(request,id):

    healthpackage = Product.objects.filter(service__name="Health Package",id=id).first()

    reviewForm = ProductReviewForm()

    canAdd = True
    if request.user.is_authenticated:
        reviewCheck = Review.objects.filter(user=request.user, product=healthpackage).count()
    else:
        pass
    if request.user.is_authenticated:
        if reviewCheck > 0:
            canAdd = False

    reviews = Review.objects.filter(product=healthpackage).order_by('-id')
    avg_reviews = Review.objects.filter(product=healthpackage).aggregate(avg_rating=Avg('review_rating'))


    related_products = Product.objects.exclude(id=id).filter(service__name="Health Package")
    context = {
        'healthpackage': healthpackage,
        'related_products': related_products,
        'form': reviewForm,
        'canAdd': canAdd,
        'reviews': reviews,
        'avg_reviews': avg_reviews,

    }

    return render(request, 'healthpackage-product.html',context)


def DiagnosticList(request):
    diagnostic = Product.objects.filter(service__name="Diagnostic").order_by('-id')
    context = {
        'diagnostic': diagnostic,
    }

    return render(request,'diagnostic-list.html',context)

def save_medcart_review(request,pid):
    product = Product.objects.get(pk=pid)
    user = request.user
    review = Review.objects.create(
        user=user,
        product=product,
        review_text=request.POST.get('review_text'),
        review_rating=request.POST.get('review_rating'),
    )

    return redirect(f'/medcart-list/{pid}')

def save_demandservice_review(request,pid):
    product = Product.objects.get(pk=pid)
    user = request.user
    review = Review.objects.create(
        user=user,
        product=product,
        review_text=request.POST.get('review_text'),
        review_rating=request.POST.get('review_rating'),
    )

    return redirect(f'/ondemandservice-list/{pid}')

def save_healthpackage_review(request,pid):
    product = Product.objects.get(pk=pid)
    user = request.user
    review = Review.objects.create(
        user=user,
        product=product,
        review_text=request.POST.get('review_text'),
        review_rating=request.POST.get('review_rating'),
    )

    return redirect(f'/healthpackage-list/{pid}')

def save_doctor_review(request,pid):
    doctor = Doctors.objects.get(pk=pid)
    user = request.user

    review = DoctorReview.objects.create(
        user=user,
        doctor=doctor,
        review_text=request.POST.get('review_text'),
        review_rating=request.POST.get('review_rating'),
    )

    return redirect(f'/doctor-list/{pid}')

def save_nurse_review(request,pid):
    nurse = Nurse.objects.get(pk=pid)
    user = request.user

    review = NurseReview.objects.create(
        user=user,
        nurse=nurse,
        review_text=request.POST.get('review_text'),
        review_rating=request.POST.get('review_rating'),
    )

    return redirect(f'/nurse-list/{pid}')



@login_required(login_url="/users/login")
def cart_add(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)

    cart.remove(product)

    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)

    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart-details.html')

def Edit(request,id):
    hp = Review.objects.get(id=id)
    if request.method == "POST":
        form = ProductReviewForm(request.POST, instance=hp)
        if form.is_valid():
            form.save()
            return redirect(f'/healthpackage-list/{hp.product.id}')
    else:
        form = ProductReviewForm(instance=hp)

        context = {
            'form': form,
            'hp':hp,
        }

        return render(request,'review-edit.html',context)

def EditReview(request,id):
    hp = Review.objects.get(id=id)
    if request.method == "POST":
        form = ProductReviewForm(request.POST, instance=hp)
        if form.is_valid():
            form.save()
            return redirect(f'/ondemandservice-list/{hp.product.id}')
    else:
        form = ProductReviewForm(instance=hp)

        context = {
            'form': form,
            'hp':hp,
        }

        return render(request,'edit_review.html',context)

def Edit_Review(request,id):
    hp = Review.objects.get(id=id)
    if request.method == "POST":
        form = ProductReviewForm(request.POST, instance=hp)
        if form.is_valid():
            form.save()
            return redirect(f'/medcart-list/{hp.product.id}')
    else:
        form = ProductReviewForm(instance=hp)

        context = {
            'form': form,
            'hp':hp,
        }
        return render(request,'edit.html',context)

def Delete(request,id):
    healthpackage = Review.objects.get(id=id)
    healthpackage.delete()
    return redirect(f'/healthpackage-list/{healthpackage.product.id}')
def DeleteReview(request,id):
    healthpackage = Review.objects.get(id=id)
    healthpackage.delete()
    return redirect(f'/ondemandservice-list/{healthpackage.product.id}')
def Delete_Review(request,id):
    healthpackage = Review.objects.get(id=id)
    healthpackage.delete()
    return redirect(f'/medcart-list/{healthpackage.product.id}')

def Test(request):

    medcart = Product.objects.filter(service__name="Medcart").order_by('-id')
    category = Category.objects.exclude(name="None")
    price_range = PriceRange.objects.all()

    context = {
        'data': medcart,
        'category': category,
        'price_range': price_range,
    }

    return render(request,'test-list.html',context)


def test_filter_data(request):
    category = request.GET.getlist('category[]')
    price = request.GET.getlist('price[]')
    medcart = Product.objects.filter(service__name="Medcart")

    if len(category) > 0:
        medcart = Product.objects.filter(service__name="Medcart",category__id__in=category).distinct().order_by('-id')
    if len(price) > 0:
        medcart = Product.objects.filter(service__name="Medcart",price_range__id__in=price).distinct().order_by('-id')


    t = render_to_string('ajax/test-list.html', {'data': medcart})

    return JsonResponse({'data': t})

def Dashboard(request,pid):

    nurse = Nurse.objects.get(pk=pid-1)
    nursehire = NurseHire.objects.filter(nurse_name=nurse)
    if request.method == 'POST':
        form = NurseInfo(request.POST, request.FILES,instance=nurse)
        if form.is_valid():
            form.save()

            return redirect(f"/dashboard/{pid}/")
    else:
        form = NurseInfo(instance=nurse)

    context = {'form': form,'nurse':nurse,'nursehire':nursehire}
    return render(request,'dashboard.html',context)

def Profile(request,pid):
    user = request.user
    nurse = CustomUser.objects.get(pk=pid)
    nursehire = PatientAppointment.objects.filter(patient_name=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES,instance=nurse)
        if form.is_valid():
            form.save()

            return redirect(f"/dashboard/{pid}/")
    else:
        form = UserForm(instance=nurse)

    context = {'form': form,'nurse':nurse,'nursehire':nursehire}
    return render(request,'user-profile.html',context)

@login_required(login_url="/login")
def Nurse_Hire(request,pid):
    nurse = Nurse.objects.get(pk = pid)
    print(nurse.is_active)

    user = request.user
    if request.method == 'POST':
        form = NurseHireForm(request.POST)
        if form.is_valid():

            nurse_name = nurse
            nurse_image = nurse.image
            service_area = form.cleaned_data['service_area']
            service_name = form.cleaned_data['service_name']
            service_obj = ServiceName.objects.get(name=service_name)
            service_price = service_obj.price
            working_time = form.cleaned_data['working_time']
            nursehire = NurseHire(
                name=user,
                service_name=service_name,
                service_area=service_area,
                working_time=working_time,
            )
            appt = Appointment(
                patient_name = user,
                nurse_name=nurse_name,
                image=nurse_image,
                service_name=service_name,
                service_price=service_price,
                service_area=service_area,
                booking_time=working_time,
            )

            nursehire.save()
            appt.save()


            return redirect("details")
    else:
        form = NurseHireForm()

    context = {'form': form,'nurse':nurse}
    return render(request,'nurse-hire.html',context)

def Nurse_Hire_Delete(request,id):
    nursehire = BookedAppointment.objects.filter(id=id).delete()
    nursehi = PatientAppointment.objects.filter(id=id).delete()
    user = request.user
    nurse = Nurse.objects.get(username=user)
    nurse.is_active = True
    nurse.save()
    return redirect('nurse_dashboard')

def Nurse_Hire_Accept(request,id):

    user = request.user
    n = Nurse.objects.get(username=user)
    appointment = BookedAppointment.objects.get(nurse_name=n.name)
    nursehire = BookedAppointment.objects.filter(id=id)
    total = int(appointment.service_price) + 15 + 50
    appt = ConfirmedAppointment(
        patient_name=appointment.patient_name,
        nurse_name=appointment.nurse_name,
        image=appointment.image,
        service_name=appointment.service_name,
        service_price=appointment.service_price,
        service_area=appointment.service_area,
        booking_time=appointment.booking_time,
        total=str(total)
    )
    nursehire.delete()
    appt.save()
    return redirect('nurse_dashboard')

def WorkedDone(request,id):

    user = request.user
    n = Nurse.objects.get(username=user)
    appointment = ConfirmedAppointment.objects.get(nurse_name=n.name)
    nursehire = ConfirmedAppointment.objects.filter(id=id)
    total = int(appointment.service_price) + 15 + 50
    appt = WorkDone(
        patient_name=appointment.patient_name,
        nurse_name=appointment.nurse_name,
        image=appointment.image,
        service_name=appointment.service_name,
        service_price=appointment.service_price,
        service_area=appointment.service_area,
        booking_time=appointment.booking_time,
        total=str(total)
    )
    nursehire.delete()
    n.is_active = True
    n.save()
    appt.save()
    return redirect('nurse_dashboard')

def Details(request):
    user = request.user
    appointment = Appointment.objects.get(patient_name=user)
    print(appointment.nurse_name)
    context = {'appointment': appointment}

    return render(request,'cart/cart-detail.html',context)


def Booked(request):
    user = request.user
    appointment = Appointment.objects.get(patient_name=user)
    n = Nurse.objects.get(name = appointment.nurse_name)
    print(n.is_active)
    n.is_active = False
    vat = 15
    other_charge = 50
    total = int(appointment.service_price) + 15 + 50
    appt = BookedAppointment(
        patient_name=user,
        nurse_name=appointment.nurse_name,
        image=appointment.image,
        service_name=appointment.service_name,
        service_price=appointment.service_price,
        service_area=appointment.service_area,
        booking_time=appointment.booking_time,
        total=str(total)
    )
    appnt = PatientAppointment(
        patient_name=user,
        nurse_name=appointment.nurse_name,
        image=appointment.image,
        service_name=appointment.service_name,
        service_price=appointment.service_price,
        service_area=appointment.service_area,
        booking_time=appointment.booking_time,
        total=str(total)
    )
    appointment.delete()
    appt.save()
    appnt.save()
    n.save()
    return redirect(f"/profile/{request.user.id}/")


def Login(request):
    if request.method == "POST":
        user = authenticate(request,
                                       username=request.POST.get('username'),
                                       password=request.POST.get('password'),)
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == "1":
                return redirect("index")
            elif user_type == "2":
                return redirect('nurse_dashboard')
            else:
                return redirect("login")
        else:
            return redirect("login")

    return render(request,'login.html')

def NurseDashboard(request):
    user = request.user
    u = Nurse.objects.get(username=user)
    nurse = BookedAppointment.objects.filter(nurse_name=u.name)
    nur = ConfirmedAppointment.objects.filter(nurse_name=u.name)
    nu = WorkDone.objects.filter(nurse_name=u.name)
    if request.method == 'POST':
        form = NurseAddForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect("nurse_dashboard")
    else:
        form = NurseAddForm(instance=user)

    context = {'nurse':nurse,'nur':nur,'nu':nu}
    return render(request,'nurse-dashboard.html',context)

