"""defines url patterns for learning_logs"""
from django.urls import path

from . import views

app_name = 'learning_logs'
app_name1 = 'https'
urlpatterns = [
    # Home page: URL with nothing between the beginning and end of the URL
    # url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),

    # show all topics
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    path(r'topics/(?P<topic_id>\d+)/', views.topic, name='topic'),

    # page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # page for adding a new entry
    path(r'new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),

    # Page for editing entry
    path(r'edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry'),

    # Button for deleting a topic in the topics page
    path(r'delete_topics/(?P<topic_id>\d+)/', views.delete_topics, name='delete_topics'),

    # Button for deleting an entry
    path(r'delete_entry/(?P<entry_id>\d+)/', views.delete_entry, name='delete_entry'),

]
