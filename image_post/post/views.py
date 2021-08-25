from django.db.models.fields.files import ImageField
from django.forms.forms import Form
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
import uuid

# Create your views here.

def index(request):
  form = ImageForm()
  context = {
    "form" : form,
    "images" : Image.objects.order_by('-created_date').all(),
  }
  return render(request, 'index.html', context)


def post(request):
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
    post = form.save()
    return redirect('/')
  return render(request, 'index.html', {'form': form})
