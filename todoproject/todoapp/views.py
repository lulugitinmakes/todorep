from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task1
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
#add to database
def add(request):
    task1=Task1.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        t=Task1(name=name,priority=priority,date=date)
        t.save()
        return redirect('/')
    return render(request,'home.html',{'task1':task1})

def base(request):
    return render(request,'base.html')

#to show in the diffrent page
#def detail(request):
#    task1=task.objects.all()
#    return render(request,'detail.html',{'task1:task1'})

def delete(request,id):
    task1 = Task1.objects.get(id=id)
    if request.method=='POST':

        task1.delete()
        return redirect('/')
    return render(request,'delete.html',{'task1':task1})


def Update(request,id):
    task=Task1.objects.get(id=id)
    form= TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})

#listView using class
class TaskListview(ListView):
    model=Task1
    template_name = 'home.html'
    context_object_name = 'task1'

class TaskDetailview(DetailView):
    model=Task1
    template_name = 'detail.html'
    context_object_name = 'task1'

class TaskUpdateview(UpdateView):
    model=Task1
    template_name='update.html'
    context_object_name = 'task1'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy("clasb_detail",kwargs={'pk':self.object.id})


class  TaskDeleteview(DeleteView):
    model=Task1
    template_name = 'delete.html'
    success_url = reverse_lazy('clasb_view')