from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
  url(r'^$', Home.as_view(), name='home'),
  url(r'^user/', include('registration.backends.simple.urls')),
  url(r'^user/', include('django.contrib.auth.urls')),
  url(r'^suggestion/create/$', SuggestionCreateView.as_view(), name='suggestion_create'),
  url(r'suggestion/$', SuggestionListView.as_view(), name='suggestion_list'),
  url(r'^suggestion/(?P<pk>\d+)/$', SuggestionDetailView.as_view(), name='suggestion_detail'),
  url(r'^suggestion/update/(?P<pk>\d+)/$', SuggestionUpdateView.as_view(), name='suggestion_update'),
  url(r'^suggestion/delete/(?P<pk>\d+)/$', SuggestionDeleteView.as_view(), name='suggestion_delete'),
  url(r'^suggestion/(?P<pk>\d+)/comment/create/$', CommentCreateView.as_view(), name='comment_create')
)
