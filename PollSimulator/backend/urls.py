from django.urls import path
from .views import *

urlpatterns = [
    path('add_candidate/', CandidateView.as_view()),
    path('cast_vote/', CasteVote.as_view()),
    path('get_results/', GetResults.as_view()),
    path('get_winner/', GetWinner.as_view()),
]
