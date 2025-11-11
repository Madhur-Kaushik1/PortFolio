from django.shortcuts import render
from .models import CV
from django.http import FileResponse

def navbar(request):
    return render(request, 'Nav/Home.html')

def Cv_fun(request):
    cv_var = CV.objects.last()
    return FileResponse(cv_var.file.open('rb'), as_attachment=True, filename="Madhur_Kaushik_CV.pdf")