#Lab1: Poll Simulator 

##Student ID: 202012017
##Student Name: Jay Kothari
##Subject: IT618 Enterprise Computing
##Lab: 1


**Using REST APIs that handles business logic, which also allows different clients to call the APIs without any change in business logic.**

Usage:
'''
# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
#or 
virtualenv env --python=python3.6   
source env/bin/activate  # On Windows use `env\Scripts\activate`

pip install -r requirements.txt
'''


To Run program, start django server 
'''
cd PollSimulator/ 

python manage.py runserver
'''

Go to: [localhost:8000](localhost:8000)



###Functionalities Implemented

####The backend folder handles all the business logic.
backend/urls.py => Handles routing for all the REST APIs 
backend/views.py => Contains the APIs code.


####List of APIs: 
GET: [http://localhost:8000/api/add_candidate/](http://localhost:8000/api/add_candidate/): List of all candidates.

POST: [http://localhost:8000/api/add_candidate/](http://localhost:8000/api/add_candidate/): Add Candidates, check added to prevent registration by same student again based on Student ID.
JSON Post Format: 
{
 "StudentID": 1234,
 "StudentName": "XYZ"
}

POST: [http://localhost:8000/api/cast_vote/](http://localhost:8000/api/cast_vote/): Cast Vote
JSON Post Format: 
{
 "StudentID": 123,
 "CandidateID": 12321
}

GET: [http://localhost:8000/api/get_results/](http://localhost:8000/api/get_results/): Gives Result

GET: [http://localhost:8000/api/get_winner/](http://localhost:8000/api/get_winner/): Gives Poll Summary



####The backend folder handles all the business logic.
frontend/urls.py => Handles routing
frontend/views.py => Just Serves the HTML page.

**All the HTML files have JQuery code inside them that calls the backend APIs.**
**The JQuery Code uses GET and POST on the above mentioned APIs to populate data.**
**frontend/views.py only serves the file and doesn't provide any data.**


####HTML pages: 
[Homepage](http://localhost:8000): frontend/index.html


[Add Candidates](http://localhost:8000/add_candidate/): frontend/add_candidate.html
Uses POST http://localhost:8000/api/add_candidate/ API to add data and displays the response


[Cast Vote](http://localhost:8000/vote/): frontend/vote.html
Uses GET http://localhost:8000/api/add_candidate/ API to list all the candidates, also checks if there are no candidates, and if so displays appropriate message and disbales Cast Vote button.

Uses POST http://localhost:8000/api/cast_vote/ API to cast vote and displats the response provided by the API


[Poll Results](http://localhost:8000/poll_results/): frontend/poll_results.html
Uses GET http://localhost:8000/api/get_results/ to GET data of winner and  runner up candidate


[Voting Summary](http://localhost:8000/voting_summary/): frontend/voting_summary.html
Uses GET http://localhost:8000/api/get_winner/ to display the summary of all the candidates in order of their votes
