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
    path('topics/topic_id/', views.topic, name='topic'),

    # page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # page for adding a new entry
    path('new_entry/topic_id/', views.new_entry, name='new_entry'),

    # Page for editing entry
    path('edit_entry/entry_id/', views.edit_entry, name='edit_entry'),

    # Button for deleting a topic in the topics page
    path('delete_topics/topic_id/', views.delete_topics, name='delete_topics'),

    # Button for deleting an entry
    path('delete_entry/entry_id/', views.delete_entry, name='delete_entry'),

]
