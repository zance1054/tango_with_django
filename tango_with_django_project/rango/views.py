from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
# Create your views here.

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    # Render the response and send it back! 
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/about.html', context=context_dict)
