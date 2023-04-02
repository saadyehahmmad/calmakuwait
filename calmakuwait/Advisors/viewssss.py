from django.shortcuts import render
from .models import advizor, Cover
from Advisors.viewssss import advizor

# Create your views here.

# Categories
def all_advisor(request):
    advisor_list = advizor.objects.filter(active=True)
    cover = Cover.objects
    context = {
        'Advisors' : advisor_list,
        'one_cover' : cover,
    }
    return render(request,'Advisors.html',context)

# Category
def advisor(request, slug):
    advisor_one = advizor.objects.get(slug=slug)
    advisor_list = advizor.objects.filter(active=True)
    context = {
        'advisor' : advisor_one,
        'Advisors' : advisor_list,
    }
    return render(request,'advisor.html',context)

