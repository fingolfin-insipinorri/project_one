from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        return render(request, 'main.html')


class DepartureView(View):
    def get(self, request, departure):
        return render(request, 'departure.html')


class TourView(View):
    def get(self, request, hotel):
        return render(request, 'tour.html')
