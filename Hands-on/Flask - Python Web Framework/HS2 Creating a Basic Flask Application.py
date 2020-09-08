from flask import Flask

## Define a flask application name 'app' below
app = Flask(__name__)

## Define below a view function 'hello', which displays the message
## "Hello World!!! I've run my first Flask application."
@app.route("/")
def hello():
   return "Hello World!!! I've run my first Flask application."

## Write the required code below which runs flask applictaion 'app' defined above
## on host 0.0.0.0 and port 8000
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)