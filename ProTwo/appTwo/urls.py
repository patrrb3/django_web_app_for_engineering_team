from django.conf.urls import url
from appTwo import views

app_name = 'appTwo'
urlpatterns = [
    url(r'^site',views.site,name='site'),
    url(r'^sales_estimate',views.sales_estimate,name='sales_estimate'),
    url(r'^upload',views.model_form_upload,name='upload'),

]
