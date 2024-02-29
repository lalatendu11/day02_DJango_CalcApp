from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,template_name="input.html")

def calculate(request):
    x = int(request.POST["t1"])
    y = int(request.POST["t2"])
    x = int(x)
    y = int(y)
    opt = request.POST["op"]
    result = ""
    if opt == 'add':
        z = x+y
        result = result + " "+str(z)
    elif opt == 'add':
        z = x-y
        result = result + " "+str(z)
    elif opt == 'add':
        z = x*y
        result = result + " "+str(z)
    else:
        z = x/y
        result = result + " " + str(z)

    # return HttpResponse(result)
    return HttpResponse("<html><h2>The sum is:</h2></html>"+ str(result))