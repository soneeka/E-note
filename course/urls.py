from django.urls import path

from .views import SubjectListView, SubjectSearchListView
urlpatterns = [
    path('subject/list', SubjectListView.as_view(), name="subject-list"),
    path('subject/list', SubjectSearchListView.as_view(), name="subject-search-list"),
]
