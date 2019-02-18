from django.shortcuts import render

def advertising(request):
    return render(request, 'capital/index.html')