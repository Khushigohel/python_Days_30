from day16_link_task import emojifier,tagify

print(__name__)
print(emojifier('hello world', 'p'))
print(tagify('python', '😍'))

#### exernal mdule
#1. Request
#Making HTTP Requests
import requests
response=requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.json())

### post method
payload={'title': 'Hello World', 'body': 'This is a post', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
if response.status_code == 200:
    print("Request successful!")
print(response.json())

import pyjokes
print(pyjokes.get_joke())