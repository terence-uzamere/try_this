from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required 
from .views import *

urlpatterns = patterns('',
  url(r'^$', Home.as_view(), name='home'),
  url(r'^user/', include('registration.backends.simple.urls')),
  url(r'^user/', include('django.contrib.auth.urls')),
  url(r'^suggestion/create/$', login_required(SuggestionCreateView.as_view()), name='suggestion_create'),
  url(r'suggestion/$', login_required(SuggestionListView.as_view()), name='suggestion_list'),
  url(r'^suggestion/(?P<pk>\d+)/$', login_required(SuggestionDetailView.as_view()), name='suggestion_detail'),
  url(r'^suggestion/update/(?P<pk>\d+)/$', login_required(SuggestionUpdateView.as_view()), name='suggestion_update'),
  url(r'^suggestion/delete/(?P<pk>\d+)/$', login_required(SuggestionDeleteView.as_view()), name='suggestion_delete'),
  url(r'^suggestion/(?P<pk>\d+)/comment/create/$', login_required(CommentCreateView.as_view()), name='comment_create'),
  url(r'^suggestion/(?P<suggestion_pk>\d+)/comment/update/(?P<comment_pk>\d+)/$', login_required(CommentUpdateView.as_view()), name='comment_update'),
  url(r'^suggestion/(?P<suggestion_pk>\d+)/comment/delete/(?P<comment_pk>\d+)/$', login_required(CommentDeleteView.as_view()), name='comment_delete'),
)
