# MicroserviceA
Microservice A - Job Matching Percentage
Overview: This microservice calculates the job matching percentage based on input keywords that describe an applicant's experience. It maps these keywords to predefined job roles and their respective matching percentages.

## Requesting Data
To request data from this microservice, send a POST request to the `/match` endpoint with a JSON payload containing keywords. The keywords should be an array of terms that describe the applicant's skills or experience.

import requests

def get_matching_percentage(keywords):
    endpoint = 'http://localhost:5000/match'
    response = requests.post(endpoint, json={'keywords': keywords})
    return response.json()

###Sample usage
keywords = ['pharmacy', 'radiology']
response = get_matching_percentage(keywords)
print(response)

## Receiving Data
The microservice responds with a JSON object that includes the highest matching percentage and the corresponding job position. If no matches are found, it will return a default message.
Response Format:
{
  "percentage": 75,
  "job_position": "Pharmacist 1 (full-time, day shift)"
}
