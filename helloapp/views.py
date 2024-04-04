from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{"name":'Professor'})

def add(request):
    val1 = float (request.POST['num1'])
    val2 = float (request.POST['num2'])
    op = request.POST["op"]
    if op == "add":
        res = val1 + val2
    elif op == "sub":
        res = val1 - val2
    elif op == "mul":
        res = val1 * val2
    elif op == "div":
        res = val1 / val2
    return render(request,'result.html',{"result":res})
