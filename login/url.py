from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^login/product', views.check_pass, name='check_pass'),
    #url(r'^login/product$', views.product, name='product'),
    url(r'^login$', views.post_list, name='post_list'),
    url(r'^$', RedirectView.as_view(url='/login')),
]
