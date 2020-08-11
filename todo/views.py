from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView
	)
from .models import Task
from django.urls import reverse


class TaskList(ListView):
	model = Task
	context_object_name = 'tasklist'
	template_name = 'todo/index.html'


class CreateTask(CreateView):
	model = Task
	fields = ['title']
	template_name = 'todo/create_task.html'

	def get_success_url(self):
		return reverse('todo:index')


class UpdateTask(UpdateView):
	model = Task
	fields = ['title']
	template_name = 'todo/update_task.html'

	def get_success_url(self):
		return reverse('todo:index')


class DeleteTask(DeleteView):
	model = Task
	template_name = 'todo/delete_task.html'

	def get_success_url(self):
		return reverse('todo:index')
