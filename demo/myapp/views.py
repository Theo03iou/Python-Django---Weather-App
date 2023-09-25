from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello world</h1>")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items })