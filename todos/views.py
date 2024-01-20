from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def index(req):
    todos=Todo.objects.all()
    print(todos)
    return render(req,"todos/base.html",  {"todos":todos})

def createTodo(req):
    if req.method=="GET":
        return render(req,"todos/form.html", {"todo":todo})
    if req.method=="POST":
        todo = req.POST["todo"]
        Todo.objects.create(todo=todo)
        print(todo)
        return redirect("/")
 
def updateTodo(req,id):
  todo = get_object_or_404(Todo,pk=id)
  if req.method=="GET":
   return render(req,"todos/update.html", {"todo":todo})
  


def createTodo(req):
#    if req.method
  return HttpResponse("Hello "+str(id))



 

   
