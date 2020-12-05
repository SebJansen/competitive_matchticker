from django.urls import path

from match.views import MatchListView, MatchDetailView

app_name = 'match'

urlpatterns = [
    path('list', MatchListView.as_view(), name='list'),
    path('<int:pk>/', MatchDetailView.as_view(), name='detail'),
]
