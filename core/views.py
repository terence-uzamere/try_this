from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import *
from .forms import *

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

  def get_object(self, *args, **kwargs):
    object = super(SuggestionUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class SuggestionDeleteView(DeleteView):
  model = Suggestion
  template_name = 'suggestion/suggestion_confirm_delete.html'
  success_url = reverse_lazy('suggestion_list')

  def get_object(self, *args, **kwargs):
    object = super(SuggestionDeleteView, self).get_objects(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

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

  def get_object(self, *args, **kwargs):
    object = super(CommentUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class CommentDeleteView(DeleteView):
  model = Comments
  pk_url_kwarg = 'answer_pk'
  template_name = 'comment/comment_confirm_delete.html'

  def get_success_url(self):
    return self.object.suggestion.get_absolute_url()

  def get_object(self, *args, **kwargs):
    object = super(CommentDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class VoteFormView(FormView):
  form_class = VoteForm

  def form_valid(self, form):
    user = self.request.user
    suggestion = Suggestion.objects.get(pk=form.data["suggestion"])
    prev_votes = Vote.objects.filter(user=user, suggestion=suggestion)
    has_voted = (prev_votes.count()>0)
    if not has_voted:
      Vote.objects.create(user=user, suggestion=suggestion)
    else:
      prev_votes[0].delete()
    return redirect('suggestion_list')