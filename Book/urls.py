from django.conf.urls import url
from Book import views

urlpatterns = [
    url(r'^borrow/$', views.borrow, name='borrow'),
    url(r'^returning/$', views.returning, name='returning'),
    url(r'^success/$', views.success),
]