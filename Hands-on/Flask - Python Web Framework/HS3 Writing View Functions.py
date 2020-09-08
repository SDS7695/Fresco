from flask import Flask

## Define a flask application name 'app' below

app = Flask(__name__)

## Define below a view function 'hello', which displays the message
## "Hello World!!! I've run my first Flask application."
## The view function 'hello' should be mapped to URL '/' .
@app.route("/")
def hello():
  return "Hello World!!! I've run my first Flask application."



## Define below a view function 'hello_user', which takes 'username' as an argument
## and returns the html string containing a 'h2' header  "Hello <username>"
## After displaying the hello message, the html string must also display one quote,
## randomly chosen from the provided list `quotes`
## Before displaying the quote, the html string must contain the 'h3' header 'Quote of the Day for You'
## The view function 'hello_user' should be mapped to URL '/hello/<username>/' .
## Use the below list 'quotes' in 'hello_user'  function
## quotes = [
##                "Only two things are infinite, the universe and human stupidity, and I am not sure about the former.",
##                "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
##                "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
##                "Listen to many, speak to a few.",
##                "Only when the tide goes out do you discover who has been swimming naked."
##    ]
@app.route("/hello/<username>/")
def hello_user(username):
  quotes = [
                "Only two things are infinite, the universe and human stupidity, and I am not sure about the former.",
                "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
                "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
                "Listen to many, speak to a few.",
                "Only when the tide goes out do you discover who has been swimming naked."
    ]
  return '''
  <html>
    <body>
        <h2>Hello ''' +username+'''</h2>
        <h3>Quote of the Day for You</h3>
        <p>'''+quotes[3]+'''</p>
    </body>
</html>'''



## Define below a view function 'display_quotes', which returns an html string
## that displays all the quotes present in 'quotes' list in a unordered list.
## Before displaying 'quotes' as an unordered list, the html string must also include a 'h1' header "Famous Quotes".
## The view function 'display_quotes' should be mapped to URL '/quotes/' .
## Use the below list 'quotes' in 'display_quotes'  function
## quotes = [
##                "Only two things are infinite, the universe and human stupidity, and I am not sure about the former.",
##                "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
##                "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
##                "Listen to many, speak to a few.",
##                "Only when the tide goes out do you discover who has been swimming naked."
##    ]
@app.route('/quotes/')
def display_quotes():
    quotes = [
                "Only two things are infinite, the universe and human stupidity, and I am not sure about the former.",
                "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
                "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
                "Listen to many, speak to a few.",
                "Only when the tide goes out do you discover who has been swimming naked."
    ]

    string = '''
    <html>
    <body>
        <h1>Famous Quotes</h1>'''
    for quote in quotes:
        string+=  '''<ul>'''+quote+'''</ul>'''
    string += '''</body>
    </html>'''
    return string



## Write the required code below which runs flask applictaion 'app' defined above
## on host 0.0.0.0 and port 8000
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)