from rest_framework.views import APIView
from rest_framework.response import Response
from operator import itemgetter

# In-Memory Data

# Candidate details will be stored in a list with the structure mentioned below
# candidates = [
#   {
#     StudentID: ,
#     StudentName: ,
#     Votes:
#   },
# ]
candidates = []

# A list will be maintained to prevent repeated voting
students_voted = []


############################
# APIs

class CandidateView(APIView):
    def get(self, request, format=None):
        return Response({"results": candidates})

    def post(self, request, format=None):
        check = next(
            (candidate for candidate in candidates if candidate['StudentID'] == request.data.get('StudentID')),
            None)

        if check is not None:
            return Response({"results": "Candidate with same Student ID already exists"})

        candidates.append({
            "StudentID": request.data.get('StudentID'),
            "StudentName": request.data.get('StudentName'),
            "Votes": 0
        })

        return Response({"results": "Candidate Registered"})


class CasteVote(APIView):
    def post(self, request, format=None):
        student_id = int(request.data.get('StudentID'))
        if student_id in students_voted:
            return Response({"results": "You have already voted!"})

        students_voted.append(student_id)
        student = next(
            (candidate for candidate in candidates if candidate['StudentID'] == request.data.get('CandidateID')),
            None)

        if student is None:
            return Response({"results": "No such candidate exists"})

        student['Votes'] = student['Votes'] + 1
        return Response({"results": "Your vote has been recorded successfully."})


class GetResults(APIView):
    def get(self, request, format=None):
        result = sorted(candidates, key=itemgetter('Votes'), reverse=True)
        return Response({'results': result})


class GetWinner(APIView):
    def get(self, request, format=None):
        result = sorted(candidates, key=itemgetter('Votes'), reverse=True)
        return Response({'results': result[:2]})
