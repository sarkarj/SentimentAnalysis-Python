import requests

url = 'http://18.217.83.127:5000/api/v1'
msg = {'message':'The book was engaging, enjoyed reading, definitely recommending'}

response = requests.post(url, json = msg)
print(response.text)

