from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
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
  fields = ['category', 'name', 'caption']
  success_url = reverse_lazy('suggestion_list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(SuggestionCreateView, self).form_valid(form)

class SuggestionListView(ListView):
  model = Suggestion
  template_name = 'suggestion/suggestion_list.html'
  paginate_by = 5

  def get_context_data(self, **kwargs):
    context = super(SuggestionListView, self).get_context_data(**kwargs)
    user_votes = Suggestion.objects.filter(vote__user=self.request.user)
    context['user_votes'] = user_votes
    return context

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
  fields = ['category', 'name', 'caption']

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
    object = super(SuggestionDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class CommentCreateView(CreateView):
  model = Comments
  template_name = 'comments/comments_form.html'
  fields = ['text']

  def get_success_url(self):
    return self.object.suggestion.get_absolute_url()

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.suggestion = Suggestion.objects.get(id=self.kwargs['pk'])
    return super(CommentCreateView, self).form_valid(form)

class CommentUpdateView(UpdateView):
  model = Comments
  pk_url_kwarg = 'comments_pk'
  template_name = 'comments/comments_form.html'
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
  template_name = 'comments/comments_confirm_delete.html'

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
    try:
        comments = Comments.objects.get(pk=form.data["comments"])
        prev_votes = Vote.objects.filter(user=user, comments=comments)
        has_voted = (prev_votes.count()>0)
        if not has_voted:
            Vote.objects.create(user=user, comments=comments)
        else:
            prev_votes[0].delete()
        return redirect(reverse('suggestion_detail', args=[form.data["suggestion"]]))
    except:
        prev_votes = Vote.objects.filter(user=user, suggestion=suggestion)
        has_voted = (prev_votes.count()>0)
        if not has_voted:
            Vote.objects.create(user=user, suggestion=suggestion)
        else:
            prev_votes[0].delete()
    return redirect('suggestion_list')

class UserDetailView(DetailView):
  model = User
  slug_field = 'username'
  template_name = 'user/user_detail.html'
  context_object_name = 'user_in_view'

  def get_context_data(self, **kwargs):
    context = super(UserDetailView, self).get_context_data(**kwargs)
    user_in_view = User.objects.get(username=self.kwargs['slug'])
    suggestions = Suggestion.objects.filter(user=user_in_view)
    context['suggestions'] = suggestions
    comments = Comments.objects.filter(user=user_in_view)
    context['comments'] = comments
    return context

class UserUpdateView(UpdateView):
  model = User
  slug_field = "username"
  template_name = 'user/user_form.html'
  fields = ['email', 'first_name', 'last_name']

  def get_success_url(self):
    return reverse('user_detail', args=[self.request.user.username])

  def get_object(self, *args, **kwargs):
    object = super(UserUpdateView, self).get_object(*args, **kwargs)
    if object != self.request.user:
      raise PermissionDenied()
    return object

class UserDeleteView(DeleteView):
  model = User
  slug_field = "username"
  template_name = 'user/user_confirm_delete.html'

  def get_success_url(self):
    return reverse_lazy('logout')

  def get_object(self, *args, **kwargs):
    object = super(UserDeleteView, self).get_object(*args, **kwargs)
    if object != self.request.user:
      raise PermissionDenied()
    return object

  def delete(self, request, *args, **kwargs):
    user = super(UserDeleteView, self).get_object(*args)
    user.is_active = False
    user.save()
    return redirect(self.get_success_url())

class SearchSuggestionListView(SuggestionListView):
  def get_queryset(self):
    incoming_query_string = self.request.GET.get('query', '')
    return Suggestion.objects.filter(category__icontains=incoming_query_string)
