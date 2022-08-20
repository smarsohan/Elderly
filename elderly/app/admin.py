from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(OnDemandServicesPrice)
admin.site.register(OnDemandServices)
#admin.site.register(Nurses)
admin.site.register(Nurse)
admin.site.register(NurseSpeciality)
admin.site.register(NurseExperience)
admin.site.register(Doctors)
admin.site.register(DoctorSpeciality)
admin.site.register(DoctorExperience)
admin.site.register(HealthPackagePrice)
admin.site.register(TrustedPartner)
admin.site.register(Medcart)
admin.site.register(MedcartCategory)
admin.site.register(MedcartPrice)
admin.site.register(HealthPackageProduct)
admin.site.register(Diagnostic)
admin.site.register(Review)
admin.site.register(DemandServiceReview)
admin.site.register(HealthPackageReview)
admin.site.register(DoctorReview)
admin.site.register(NurseReview)
admin.site.register(HealthpackageAvgReview)
admin.site.register(Product)
admin.site.register(Services)
admin.site.register(Category)
admin.site.register(PriceRange)
admin.site.register(Area)
admin.site.register(WorkingTime)
admin.site.register(ServiceName)
admin.site.register(NurseHire)
admin.site.register(Appointment)
admin.site.register(BookedAppointment)
admin.site.register(ConfirmedAppointment)
admin.site.register(WorkDone)
admin.site.register(PatientAppointment)