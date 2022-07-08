from django.shortcuts import render, HttpResponseRedirect
from .forms import ImageForm
from .models import Image

def Home(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all()
 return render(request, 'home.html', {'img':img, 'form':form})

def Delete_pic(request, id):
    img = Image.objects.get(pk=id)
    img.delete()
    return HttpResponseRedirect('/')
    