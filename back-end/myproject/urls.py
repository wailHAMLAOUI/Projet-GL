from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from myproject import views
# import rest_framework

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('',TemplateView.as_view(template_name='index.html'))
]
