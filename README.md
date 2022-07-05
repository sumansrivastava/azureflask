# Building your Flask application.
1. To Build your flask application the first thing you need is python setup.
```
sudo apt-get update 
sudo apt-get install python3 python3-venv python3-pip 
sudo pip install flask
```
2. Create your first app.py file
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def hello():
    return '<h1>Welcom! You are here that means you hosted well !!</h1>'

@app.route('/about/')
def about():
    return '<h2>If you are seeing this pages. Conratulations your webapp is routeing fine.</h2>'
```
3. Run and Test your application
```
export FLASK_APP=app.py
flask run
```
```
Go to http://localhost:5000
```
4. Now when you have tested your application on localhost. It's time to create an image to run your application as container.
```
FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```
5. Lets create our first docker build.
```
docker build -t <application_name>:tag_version /location/of/dockerfile
```
6. Let's now test the application running as container
```
docker run -d --name <app_name> -p 80:5000 <application_name>:tag_version
```
```
Go to http://localhost
```

### Since, you have built and tested your application on flask and hosted them well in container, it's time to run the application on Azure Container Instance. We are going to use terraform to automate this entire suite.
