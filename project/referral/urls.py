from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from referral import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.HomeView.as_view()), name='home'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^signup$', views.SignupView.as_view(), name='signup'),
    url(r'^logout$', views.user_logout, name='logout'),
)
