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
  url(r'^vote/$', login_required(VoteFormView.as_view()), name='vote'),
  url(r'^user/(?P<slug>\w+)/$', login_required(UserDetailView.as_view()), name='user_detail'),
  url(r'^user/update/(?P<slug>\w+)/$', login_required(UserUpdateView.as_view()), name='user_update'),
  url(r'^user/delete/(?P<slug>\w+)/$', login_required(UserDeleteView.as_view()), name='user_delete'),
  url(r'^search/$', login_required(SearchSuggestionListView.as_view()), name='search'),
)
