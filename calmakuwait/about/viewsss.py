from django.shortcuts import render,redirect
from .models import About, Cover
# from .forms import ContactForm

# Create your views here.

def about_one(request):
    about_last = About.objects.filter(active=True)
    cover = Cover.objects.latest('id')
    context = {
        'about' : about_last,
        'one_cover' : cover,
    }
    return render(request,'about.html',context)


# def submit_form(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('about')
#     else:
#         form = ContactForm()

#     return render(request, 'about.html', {'form': form})
