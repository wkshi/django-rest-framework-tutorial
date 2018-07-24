from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from snippets import views

from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Pastebin API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls))
]


#from django.conf.urls import url, include
#from snippets.views import SnippetViewSet, UserViewSet, api_root
#from rest_framework import renderers
#
#from rest_framework.urlpatterns import format_suffix_patterns
#
#snippet_list = SnippetViewSet.as_view({
#    'get': 'list',
#    'post': 'create'
#})
#snippet_detail = SnippetViewSet.as_view({
#    'get': 'retrieve',
#    'put': 'update',
#    'patch': 'partial_update',
#    'delete': 'destroy'
#})
#snippet_highlight = SnippetViewSet.as_view({
#    'get': 'highlight'
#}, renderer_classes=[renderers.StaticHTMLRenderer])
#user_list = UserViewSet.as_view({
#    'get': 'list'
#})
#user_detail = UserViewSet.as_view({
#    'get': 'retrieve'
#})
#
#
#urlpatterns = format_suffix_patterns([
#    url(r'^$', api_root),
#    url(r'^snippets/?$', snippet_list, name='snippet-list'),
#    url(r'^snippets/(?P<pk>[0-9]+)/?$', snippet_detail, name='snippet-detail'),
#    url(r'^snippets/(?P<pk>[0-9]+)/highlight/?$', snippet_highlight, name='snippet-highlight'),
#    url(r'^users/?$', user_list, name='user-list'),
#    url(r'^users/(?P<pk>[0-9]+)/?$', user_detail, name='user-detail')
#])


#from django.conf.urls import url, include
#from rest_framework.urlpatterns import format_suffix_patterns
#from snippets import views
#
## API endpoints
#urlpatterns = format_suffix_patterns([
#    url(r'^$', views.api_root),
#    url(r'^snippets/?$',
#        views.SnippetList.as_view(),
#        name='snippet-list'),
#    url(r'^snippets/(?P<pk>[0-9]+)/?$',
#        views.SnippetDetail.as_view(),
#        name='snippet-detail'),
#    url(r'^snippets/(?P<pk>[0-9]+)/highlight/?$',
#        views.SnippetHighlight.as_view(),
#        name='snippet-highlight'),
#    url(r'^users/?$',
#        views.UserList.as_view(),
#        name='user-list'),
#    url(r'^users/(?P<pk>[0-9]+)/?$',
#        views.UserDetail.as_view(),
#        name='user-detail')
#])


#from django.conf.urls import url
#from rest_framework.urlpatterns import format_suffix_patterns
#from snippets import views
#
#
#urlpatterns = [
#    url(r'^$', views.api_root),
#    url(r'^snippets/?$', views.SnippetList.as_view()),
#    url(r'^snippets/(?P<pk>[0-9]+)/?$', views.SnippetDetail.as_view()),
#    url(r'^snippets/(?P<pk>[0-9]+)/highlight/?$', views.SnippetHighlight.as_view()),
#    url(r'^users/?$', views.UserList.as_view()),
#    url(r'^users/(?P<pk>[0-9]+)/?$', views.UserDetail.as_view()),
#]
#
#urlpatterns = format_suffix_patterns(urlpatterns)


#from django.conf.urls import url
#from rest_framework.urlpatterns import format_suffix_patterns
#from snippets import views
#
#urlpatterns = [
#    url(r'^snippets/$', views.snippet_list),
#    url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
#]
#
#urlpatterns = format_suffix_patterns(urlpatterns)


#from django.conf.urls import url
#from snippets import views
#
#urlpatterns = [
#    url(r'^snippets/$', views.snippet_list),
#    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
#]
