from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html')


def addCandidate(request):
    return render(request, 'frontend/add_candidate.html')


def vote(request):
    return render(request, 'frontend/vote.html')


def pollResults(request):
    return render(request, 'frontend/poll_results.html')


def votingSummary(request):
    return render(request, 'frontend/voting_summary.html')

