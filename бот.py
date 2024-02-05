Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... 
... bot_token = "6568024314:AAFNn6rCLHJmlGK1oyKUQI5mGoNIZi5RC0Q"
... url = "https://script.google.com/macros/s/AKfycbxAaHXw4GYyoFaJytcnEu-4dSjjSrN9h55lUdM4tIS3WtferMHUXHib3xglKl1eelR_Ow/exec"
... 
... user_message = "Hello, Google Sheets!"
... 
... data = {
...     "message": {"text": user_message}
... }
... 
... response = requests.post(url, json=data)
... print(response.json())
