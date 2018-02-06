from django.conf.urls import url
from django.contrib import admin
from main.views import TradeForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    url(r'^trade/create/$',
        login_required(TradeForm.as_view(template_name='main/trade_form.html'))),
]
