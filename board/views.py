from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from board.models import Board
from hitcount.views import HitCountDetailView
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from mysite.views import OwnerOnlyMixin

# Create your views here.
class BoardLV(ListView):
    model = Board
    template_name = 'board/board_all.html'
    context_object_name = 'boards'
    paginate_by = 10
    
class BoardContentView(DetailView):
    model = Board
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context
    
class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    fields = ['title', 'slug', 'owner', 'content']
    initial = {'slug': 'auto-filling-do-not-input'} 
    success_url = reverse_lazy('board:index')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BoardChangeLV(LoginRequiredMixin, ListView):
    template_name = 'board/board_change_list.html'
    
    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)


class BoardUpdateView(OwnerOnlyMixin, UpdateView):
    model = Board
    fields = ['id', 'title', 'slug', 'owner', 'content']
    success_url = reverse_lazy('board:index')


class BoardDeleteView(OwnerOnlyMixin, DeleteView) :
    model = Board
    success_url = reverse_lazy('board:index')
    
  
class BoardCountHitDetailView(HitCountDetailView):
    model = Board        # your model goes here
    count_hit = True