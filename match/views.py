from django.views.generic import DetailView
from django.views.generic.list import ListView

from match.models import Match


class MatchDetailView(DetailView):
    model = Match
    template_name = 'match/match_detail.html'


class MatchListView(ListView):
    model = Match
    template_name = 'match/match_list.html'
