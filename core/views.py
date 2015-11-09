from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
  template_name = 'home.html'

class SuggestionCreateView(CreateView):
  model = Suggestion
  template_name = 'suggestion/suggestion_form.html'
  fields = ['category', 'caption']
  success_url = reverse_lazy('try_list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(SuggestionCreateView, self).form_valid(form)

class SuggestionListView(ListView):
  model = Suggestion
  template_name = 'suggestion/suggestion_list.html'

class SuggestionDetailView(DetailView):
  model = Suggestion
  template_name = 'suggestion/suggestion_detail.html'
  
  def get_context_data(self, **kwargs):
    context = super(SuggestionDetailView, self).get_context_data(**kwargs)
    suggestion = Suggestion.objects.get(id=self.kwargs['pk'])
    comments = Comments.objects.filter(suggestion=suggestion)
    context['comments'] = comments
    return context

class SuggestionUpdateView(UpdateView):
  model = Suggestion
  template_name = 'suggestion/suggestion_form.html'
  fields = ['category', 'caption']

class SuggestionDeleteView(DeleteView):
  model = Suggestion
  template_name = 'suggestion/suggestion_confirm_delete.html'
  success_url = reverse_lazy('suggestion_list')

class CommentCreateView(CreateView):
  model = Comments
  template_name = 'comment/comment_form.html'
  fields = ['text']

  def get_success_url(self):
    return self.object.question.get_absolute_url()

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.suggestion = Suggestion.objects.get(id=self.kwargs['pk'])
    return super(SuggestionCreateView, self).form_valid(form)

class CommentUpdateView(UpdateView):
  model = Comments
  pk_url_kwarg = 'answer_pk'
  template_name = 'comment/comment_form.html'
  fields = ['text']

  def get_success_url(self):
    return self.object.suggestion.get_absolute_url()
  
class CommentDeleteView(DeleteView):
  model = Comments 
  pk_url_kwarg = 'answer_pk'
  template_name = 'comment/comment_confirm_delete.html'
  
  def get_success_url(self):
    return self.object.suggestion.get_absolute_url()