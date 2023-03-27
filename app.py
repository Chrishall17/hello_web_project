import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# Declares a route that listens for a GET request to the path /
@app.route('/', methods=['GET'])
def index():
    # The code here is executed when a request is received and we need to 
    # send a response. 

    # We can return a string which will be used as the response content.
    # Unless specified, the response status code will be 200 (OK).
    return 'Some response data'

@app.route('/', methods=['POST'])
def post_index():
    # DOES NOT RUN: The HTTP method (GET) doesn't match the route's (POST)
    return "Not me! :("

@app.route('/hello', methods=['GET'])
def get_hello():
    # DOES NOT RUN: The path (`/hello`) doesn't match the route's (`/`)
    return "Not me either!"

@app.route('/', methods=['GET'])
def get_index():
    # RUNS: This route matches! The code inside the block will be executed now.
    return "I am the chosen one!"

@app.route('/', methods=['GET'])
def other_get_index():
    # DOES NOT RUN: This route also matches, but will not be executed.
    # Only the first matching route (above) will run.
    return "It isn't me, the other route stole the show"

from flask import Flask, request # NOTE: we must import `request` too


# Request:
# GET /hello?name=David

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'
    

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

# To make a request, run:
# curl "http://localhost:5000/hello?name=David"

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']

    return f"I am waving at {name}"


@app.route('/names', methods=['GET'])
def names():
    name = request.args['name']
    names = ['Julia', 'Alice', 'Karim']
    names += [name]

    return ", ".join(names)


# Request:
# POST /goodbye
#   With body parameter: name=Alice

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name'] # The value is 'Alice'
    message = request.form['message']
    
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(text)):
        if text[i] in vowels:
            count += 1    

    return f'There are {count} vowels in "{text}"'


@app.route('/sort-names', methods=['POST'])
def sort_names():
    names = request.form['names'].split(',')
    names_sorted = sorted(names)
    return ','.join(names_sorted)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


