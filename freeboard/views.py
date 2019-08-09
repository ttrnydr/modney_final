from django.shortcuts import render
from .models import Freeboard
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class BoardLV(ListView):
    model= Freeboard

class BoardDV(DetailView):
    model = Freeboard

class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Freeboard
    fields = ['title', 'body', 'image', 'star']
    success_url = reverse_lazy('freeboard:board')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BoardCreateView, self).form_valid(form)

class BoardChangeLV(LoginRequiredMixin, ListView):
    template_name = 'freeboard/freeboard_change_list.html'

    def get_queryset(self):
        return Freeboard.objects.filter(owner=self.request.user)

class BoardUpdateView(LoginRequiredMixin, UpdateView):
    model = Freeboard
    fields = fields = ['title', 'body', 'image', 'star']
    success_url = reverse_lazy('freeboard:index')

class BoardDeleteView(LoginRequiredMixin, DeleteView):
    model = Freeboard
    success_url = reverse_lazy('freeboard:index')