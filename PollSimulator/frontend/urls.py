from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('add_candidate/', addCandidate),
    path('vote/', vote),
    path('poll_results/', pollResults),
    path('voting_summary/', votingSummary),
]
