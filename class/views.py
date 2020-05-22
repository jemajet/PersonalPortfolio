from django.shortcuts import render, get_object_or_404
from .models import Class


# Create your views here.
def allclasses(request):
    classes = Class.objects
    #course_6, girs = split_classes(classes)
    return render(request, 'class/allclasses.html', {"classes": classes})


def detail(request, class_id):
    cur_class = get_object_or_404(Class, pk=class_id)
    return render(request, 'class/detail.html', {"cur_class": cur_class})


# def split_classes(classes):
#     course_6 = []
#     non_course_6 = []
#     for c in classes:
#         if "6." in c.title:
#             course_6.append(c)
#         else:
#             non_course_6.append(c)
#     return course_6, non_course_6
