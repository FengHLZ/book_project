from django.conf.urls import url
from Book import views

urlpatterns = [
    url(r'^borrow/$', views.borrow, name='borrow'),
    url(r'^returning/$', views.returning, name='returning'),
    url(r'^success/$', views.success),
    url(r'^manual/$', views.manual, name='manual'),
    url(r'^searchbook/$', views.searchbook, name='searchbook'),
]