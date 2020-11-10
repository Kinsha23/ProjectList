from django.shortcuts import render
from .models import Restaurant
# Create your views here.


def restaurant_list(request):
	context = {
		"restaurants": Restaurant.objects.all(),
	}
	return render (request, 'restaurant_list.html', context)


def restaurant_detail(request, restaurant_id):
	context = {
		"restaurant": Restaurant.objects.get(id=restaurant_id),
	}
	return render (request, 'restaurant_detail.html', context)