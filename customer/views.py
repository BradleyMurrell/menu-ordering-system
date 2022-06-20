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

class Drinks(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/drinks.html')

class Buns(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/buns.html')

class Meat(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/meat.html')

class Salad(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/salad.html')

class Dressing(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/dressing.html')
