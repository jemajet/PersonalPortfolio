from django.shortcuts import render, get_object_or_404
from .models import Class


# Create your views here.
def allclasses(request):
    classes = Class.objects
    return render(request, 'class/allclasses.html', {"classes": classes})


def detail(request, class_id):
    cur_class = get_object_or_404(Class, pk=class_id)
    return render(request, 'class/detail.html', {"cur_class": cur_class})
