from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from bookauth import views

urlpatterns= [
    url('^book/$',views.BookList.as_view()),
    url('^book/(?P<pk>[0-9]+)/$',views.BookDetail.as_view()),
    url('^author/$', views.AuthorList.as_view()),
    url('^author/(?P<pk>[0-9]+)/$', views.AuthorDetail.as_view()),

]

urlpatterns= format_suffix_patterns(urlpatterns)
