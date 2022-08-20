"""elderly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views
from forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index, name='index'),
    path('services/',views.Services, name='services'),
    path('nurse-list/',views.NurseList, name='nurse-list'),
    path('about/',views.About, name='about'),
    path('contact/',views.Contact, name='contact'),
    path('healthpackage-list/',views.HealthPackageList, name='health_package-list'),
    path('doctor-list/',views.DoctorList, name='doctor-list'),
    path('medcart-list/',views.MedcartList, name='medcart-list'),
    path('medcart-list/<str:id>',views.MedcartProduct, name='medcart-product'),
    path('filter-data',views.filter_data,name='filter-data'),
    path('nurse-filter-data',views.nurse_filter_data,name='nurse-filter-data'),
    path('medcart-filter-data',views.medcart_filter_data,name='medcart-filter-data'),
    path('healthpackage-filter-data',views.healthpackage_filter_data,name='healthpackage-filter-data'),
    path('doctor-list/<str:id>',views.DoctorProfile, name='doctor-profile'),
    path('nurse-list/<str:id>',views.NurseProfile, name='nurse-profile'),
    path('ondemandservice-list/',views.OnDemandServiceList, name='ondemandservice-list'),
    path('demandservice-filter-data',views.demandservice_filter_data,name='demandservice-filter-data'),
    path('ondemandservice-list/<str:id>',views.OnDemandServiceProduct, name='ondemandservice-product'),
    path('healthpackage-list/<str:id>',views.healthpackageproduct, name='healthpackage-product'),
    path('diagnostic-list/', views.DiagnosticList, name='diagnostic-list'),
    path('save-medcart-review/<int:pid>', views.save_medcart_review, name='save-medcart-review'),
    path('save-demandservice-review/<int:pid>', views.save_demandservice_review, name='save-demandservice-review'),
    path('save-healthpackage-review/<int:pid>', views.save_healthpackage_review, name='save-healthpackage-review'),
    path('save-doctor-review/<int:pid>', views.save_doctor_review, name='save-doctor-review'),
    path('save-nurse-review/<int:pid>', views.save_nurse_review, name='save-nurse-review'),
    path('add-nurse/', views.AddNurse, name='add-nurse'),
    path('dashboard/<int:pid>/', views.Dashboard, name='dashboard'),
    path('nurse-hire/<int:pid>', views.Nurse_Hire, name='nurse-hire'),
    path('nurse-hire-delete/<int:id>', views.Nurse_Hire_Delete, name='nurse-hire-delete'),
    path('nurse-hire-accept/<int:id>', views.Nurse_Hire_Accept, name='nurse-hire-accept'),
    path('work-done/<int:id>', views.WorkedDone, name='work-done'),

    path('edit/<str:id>', views.Edit, name='edit'),
    path('edit-review/<str:id>', views.EditReview, name='edit-review'),
    path('edit_review/<str:id>', views.Edit_Review, name='edit_review'),
    path('delete/<str:id>', views.Delete, name='delete'),
    path('delete-review/<str:id>', views.DeleteReview, name='delete-review'),
    path('delete_review/<str:id>', views.Delete_Review, name='delete_review'),

    path('details/', views.Details, name='details'),
    path('profile/<int:pid>/', views.Profile, name='profile'),
    path('booked/', views.Booked, name='booked'),

    #Test
    path('test-list/',views.Test, name='test-list'),
    path('test-filter-data',views.test_filter_data,name='test-filter-data'),


    # Authentication Url
    #path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=LoginForm), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path('accounts/register/', views.signup, name="signup"),

    path('login', views.Login, name="login"),
    path('nurse-dashboard', views.NurseDashboard, name="nurse_dashboard"),

    # Cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),



]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
