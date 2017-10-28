from django.conf.urls import url
from SDapp import views

urlpatterns = [
    url(r'^list_customers/',views.list_users,name='list_users'),
]