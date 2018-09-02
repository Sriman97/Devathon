from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
	path('check',views.login_it , name='login'),
	path('', TemplateView.as_view(template_name='login.html'), name='login'),
	path('getfine',views.librarianfine,name='getfine'),
	path('returnbook',views.librarian,name='returnbook'),    # path('admin/', admin.site.urls),
    # path('accounts/',include('django.contrib.auth.urls')),
]