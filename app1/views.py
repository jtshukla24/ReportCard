from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.

def get_students(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset =  queryset.filter(
            Q(student_name__icontains = search)|
            Q(department__department__icontains=search) |
            Q(student_id__student_id__icontains=search) |
            Q(student_email__icontains=search) |
            Q(student_age__icontains=search) )

    paginator = Paginator(queryset, 10)

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'students.html', {'queryset': page_obj})
