from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request , 'fees1.html')
def fees_python(request):
    return render(request , 'fees2.html')
