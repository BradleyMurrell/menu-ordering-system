from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order.html')

class Confirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/confirmation.html')

class Sides(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/sides.html')
