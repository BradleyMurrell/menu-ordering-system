"""brads_burgers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer.views import Index, Order, Confirmation, Sides, Drinks, Buns, Meat, Salad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('order/', Order.as_view(), name='order'),
    path('confirmation/', Confirmation.as_view(), name='confirmation'),
    path('sides/', Sides.as_view(), name='sides'),
    path('drinks/', Drinks.as_view(), name='drinks'),
    path('buns/', Buns.as_view(), name='buns'),
    path('meat/', Meat.as_view(), name='meat'),
    path('salad/', Salad.as_view(), name='salad'),
]
