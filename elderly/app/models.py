import datetime

from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
    USER = (
        (1,'PATIENT'),
        (2, 'NURSE'),
    )

    user_type = models.CharField(choices=USER,max_length=50,default=1)

class OnDemandServicesPrice(models.Model):
    price_range = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'On Demand Services Price'

    def __str__(self):
        return self.price_range

class OnDemandServices(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/DemandServices',default=None)
    price = models.CharField(max_length=100)
    price_range = models.ForeignKey(OnDemandServicesPrice, on_delete=models.CASCADE, default=True)
    description = models.TextField(max_length=5000,null=True)

    class Meta:
        verbose_name_plural = 'On Demand Services'

    def __str__(self):
        return self.name


class NurseSpeciality(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Nurse Speciality'

    def __str__(self):
        return self.name

class NurseExperience(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Nurse Experience'

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Service Area'

    def __str__(self):
        return self.name

class WorkingTime(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Working Time'

    def __str__(self):
        return self.name


class Nurses(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/Nurses', default=None)
    speciality = models.ForeignKey(NurseSpeciality, on_delete=models.CASCADE, default=True,related_name='speciality')
    price = models.CharField(max_length=100)
    introduction = models.CharField(max_length=300, default=None)
    height = models.CharField(max_length=100, default=None)
    weight = models.CharField(max_length=100, default=None)
    p_developement = models.CharField(max_length=100, default=None)
    education = models.CharField(max_length=200, default=None)
    experience = models.ForeignKey(NurseExperience, on_delete=models.CASCADE, default=True, related_name='experience')
    language = models.CharField(max_length=200, default=None)

    class Meta:
        verbose_name_plural = 'Nurses'

    def __str__(self):
        return self.name


class Nurse(models.Model):
    username = models.CharField(max_length=100,default=None)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/Nurse', default=None)
    speciality = models.ForeignKey(NurseSpeciality, on_delete=models.CASCADE, default=True,related_name='specialities')

    introduction = models.CharField(max_length=300, default=None)
    p_developement = models.CharField(max_length=100, default=None)
    education = models.CharField(max_length=200, default=None)
    experience = models.ForeignKey(NurseExperience, on_delete=models.CASCADE, default=True, related_name='experiences')
    language = models.CharField(max_length=200, default=None)
    service_area = models.ForeignKey(Area, on_delete=models.CASCADE, default=None)
    working_time = models.ForeignKey(WorkingTime, on_delete=models.CASCADE, default=None)
    is_active = models.BooleanField(verbose_name="Is Active?",default=True)


    class Meta:
        verbose_name_plural = 'Nurse'

    def __str__(self):
        return self.name


class DoctorSpeciality(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Doctor Speciality'

    def __str__(self):
        return self.name

class DoctorExperience(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Doctor Experience'

    def __str__(self):
        return self.name

class Doctors(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/Doctors',default=None)
    specialities = models.ForeignKey(DoctorSpeciality, on_delete=models.CASCADE, default=True,related_name='speciality')
    position = models.CharField(max_length=100,default=None)
    clinic_price = models.CharField(max_length=100,default=None)
    online_price = models.CharField(max_length=100,default=None)
    statement = models.CharField(max_length=600,default=None)
    bmdc_number = models.CharField(max_length=100,default=None)
    education = models.CharField(max_length=600,default=None)
    experience = models.ForeignKey(DoctorExperience, on_delete=models.CASCADE, default=True, related_name='experience')


    class Meta:
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return self.name



class HealthPackagePrice(models.Model):
    price_range = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Health Package Price Range'

    def __str__(self):
        return self.price_range


class HealthPackageProduct(models.Model):

    name = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='Images/HealthPackage', default=None)
    price = models.CharField(max_length=100)
    price_range = models.ForeignKey(HealthPackagePrice, on_delete=models.CASCADE, default=None)
    description = models.TextField(max_length=5000, null=True)

    class Meta:
        verbose_name_plural = 'Health Package Product'

    def __str__(self):
        return self.name


class TrustedPartner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/TrustedPartner', default=None)

    class Meta:
        verbose_name_plural = 'Trusted Partner'

    def __str__(self):
        return self.name

class MedcartCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Medcart Category'

    def __str__(self):
        return self.name

class MedcartPrice(models.Model):
    price_range = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Medcart Price'

    def __str__(self):
        return self.price_range

class Medcart(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/Medcart', default=None)
    price = models.CharField(max_length=100)
    price_range = models.ForeignKey(MedcartPrice, on_delete=models.CASCADE, default=True)
    category = models.ForeignKey(MedcartCategory, on_delete=models.CASCADE, default=True)
    description = models.TextField(max_length=5000, null=True)

    class Meta:
        verbose_name_plural = 'Medcart'

    def __str__(self):
        return self.name

class Diagnostic(models.Model):
    status = (('In Stock', 'In Stock'), ('Out Sock', 'Out Stock'))
    status_tag = (('in-stock', 'in-stock'), ('out-of-stock', 'out-of-stock'))
    cart_tag = (('none', 'none'), ('disabled', 'disabled'))

    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/Diagnostic',null=True)
    status = models.CharField(choices=status, null=True, max_length=100)
    status_tag = models.CharField(choices=status_tag, null=True, max_length=100)
    cart_tag = models.CharField(choices=cart_tag, default=None, max_length=100)

    class Meta:
        verbose_name_plural = 'Diagnostic'

    def __str__(self):
        return self.name

RATING = (
        ('10', '10'),
        ('20', '20'),
        ('30', '30'),
        ('40', '40'),
        ('50', '50'),
        ('60', '60'),
        ('70', '70'),
        ('80', '80'),
        ('90', '90'),
        ('100', '100'),
    )


class DemandServiceReview(models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    demandservice= models.ForeignKey(OnDemandServices,on_delete=models.CASCADE)
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)

    class Meta:
        verbose_name_plural='Demand Service Reviews'

    def __str__(self):
        return self.demandservice.name

class HealthPackageReview(models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    healthpackage= models.ForeignKey(HealthPackageProduct,on_delete=models.CASCADE)
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)

    class Meta:
        verbose_name_plural='Health Package Reviews'

    def __str__(self):
        return self.healthpackage.name

class DoctorReview(models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    doctor= models.ForeignKey(Doctors,on_delete=models.CASCADE)
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)

    class Meta:
        verbose_name_plural='Doctors Reviews'

    def __str__(self):
        return self.doctor.name

class NurseReview(models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    nurse= models.ForeignKey(Nurse,on_delete=models.CASCADE)
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)

    class Meta:
        verbose_name_plural='Nurses Reviews'

    def __str__(self):
        return self.nurse.name

class HealthpackageAvgReview(models.Model):
    healthpackage= models.ForeignKey(HealthPackageProduct,on_delete=models.CASCADE)
    avg_review = models.CharField(max_length=100,null=True)

    class Meta:
        verbose_name_plural = 'Health Package Avg Review'

    def __str__(self):
        return str(self.healthpackage)


class Services(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name

class PriceRange(models.Model):
    price_range = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Price Range'

    def __str__(self):
        return self.price_range


class Product(models.Model):
    status = (('In Stock', 'In Stock'), ('Out Sock', 'Out Stock'))
    status_tag = (('in-stock', 'in-stock'), ('out-of-stock', 'out-of-stock'))
    cart_tag = (('none', 'none'), ('disabled', 'disabled'))

    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/Product', null=True)
    service = models.ForeignKey(Services,on_delete=models.CASCADE,default=None)
    status = models.CharField(choices=status, null=True, max_length=100)
    status_tag = models.CharField(choices=status_tag, null=True, max_length=100)
    cart_tag = models.CharField(choices=cart_tag, null=True, max_length=100)
    price_range = models.ForeignKey(PriceRange, on_delete=models.CASCADE, default=None,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None,null=True)
    description = models.CharField(max_length=500)


    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.name


class Review(models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)

    class Meta:
        verbose_name_plural='Reviews'

    def __str__(self):
        return self.product.name


class ServiceName(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100,default=None)

    class Meta:
        verbose_name_plural = 'Service Name'

    def __str__(self):
        return self.name

class NurseHire(models.Model):

    name = models.CharField(max_length=100)
    service_name = models.ForeignKey(ServiceName, on_delete=models.CASCADE, default=None)
    service_area = models.ForeignKey(Area, on_delete=models.CASCADE, default=None)
    working_time = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Nurse Hire'

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    nurse_name = models.CharField(max_length=100,default=None)
    image = models.ImageField(upload_to='Images/Nurses', null=True)
    service_name = models.CharField(max_length=100)
    service_price = models.CharField(max_length=100)
    service_area = models.CharField(max_length=100)
    booking_time = models.CharField(max_length=100)


    class Meta:
        verbose_name_plural = 'Appointment'

    def __str__(self):
        return self.patient_name

class BookedAppointment(models.Model):
    patient_name = models.CharField(max_length=100)
    nurse_name = models.CharField(max_length=100,default=None)
    image = models.ImageField(upload_to='Images/Nurses', null=True)
    service_name = models.CharField(max_length=100)
    service_price = models.CharField(max_length=100)
    service_area = models.CharField(max_length=100)
    booking_time = models.CharField(max_length=100)
    total = models.CharField(max_length=100, default=None)

    class Meta:
        verbose_name_plural = 'Booked Appointment'

    def __str__(self):
        return self.patient_name


class ConfirmedAppointment(models.Model):
    patient_name = models.CharField(max_length=100)
    nurse_name = models.CharField(max_length=100,default=None)
    image = models.ImageField(upload_to='Images/Nurses', null=True)
    service_name = models.CharField(max_length=100)
    service_price = models.CharField(max_length=100)
    service_area = models.CharField(max_length=100)
    booking_time = models.CharField(max_length=100)
    total = models.CharField(max_length=100, default=None)

    class Meta:
        verbose_name_plural = 'Confirmed Appointment'

    def __str__(self):
        return self.nurse_name

class WorkDone(models.Model):
    patient_name = models.CharField(max_length=100)
    nurse_name = models.CharField(max_length=100,default=None)
    image = models.ImageField(upload_to='Images/Nurses', null=True)
    service_name = models.CharField(max_length=100)
    service_price = models.CharField(max_length=100)
    service_area = models.CharField(max_length=100)
    booking_time = models.CharField(max_length=100)
    total = models.CharField(max_length=100, default=None)

    class Meta:
        verbose_name_plural = 'Working History'

    def __str__(self):
        return self.nurse_name

class PatientAppointment(models.Model):
    patient_name = models.CharField(max_length=100)
    nurse_name = models.CharField(max_length=100,default=None)
    image = models.ImageField(upload_to='Images/Nurses', null=True)
    service_name = models.CharField(max_length=100)
    service_price = models.CharField(max_length=100)
    service_area = models.CharField(max_length=100)
    booking_time = models.CharField(max_length=100)
    total = models.CharField(max_length=100, default=None)

    class Meta:
        verbose_name_plural = 'Patient Appointment'

    def __str__(self):
        return self.patient_name