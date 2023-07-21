import requests

parameters = {
    "amount": 10,
    "type": "boolean",  # true/false question
    "category": 17  # this stands for topic science&nature
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
data = response.json()
question_data = data['results']

