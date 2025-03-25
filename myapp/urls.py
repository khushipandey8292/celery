from django.urls import path
from myapp import views
urlpatterns = [
    path('uploads/',views.upload_all_csv,name='upload_csv')
    # path('',views.index,name='home'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
]
