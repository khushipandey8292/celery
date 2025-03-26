from django.urls import path
from myapp import views
urlpatterns = [
    path('start_uploads/',views.start_csv_process,name='start_upload')
    # path('',views.index,name='home'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
 ]
