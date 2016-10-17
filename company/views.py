from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Company

# Create your views here.

class CompanyCreateView(CreateView):
    model = Company
