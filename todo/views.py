from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import UpdateView, ListView, DetailView, CreateView, DeleteView
from .models import TodoModel
from django.urls import reverse_lazy
# Create your views here.
def todo(request):
    return HttpResponse('')

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetails(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duadate')
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duadate')
    success_url = reverse_lazy('list')
