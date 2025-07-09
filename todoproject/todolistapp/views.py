from django.shortcuts import render , redirect
from django.http import HttpResponse
from . models import Todolist
from . forms import TodoForm
# Create your views here.

def index(request):
	form=TodoForm()
	lists=Todolist.objects.all()
	if request.method=='POST':
		form=TodoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context={'tasks':lists, 'TodoForm': form}
	return render(request,'todolistapp.html',context)


def updatetask(request, temp):
    task = Todolist.objects.get(id=temp)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm(instance=task)
    context = {'TaskForm': form}
    return render(request, 'update.html', context)

def deletetask(request, temp):
	task=Todolist.objects.get(id=temp)
	if request.method=='POST':
			task.delete()
			return redirect('/')
	context={'task':task}
	return render(request,'delete.html',context)