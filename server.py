"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISS = [
    'not awesome', 'not terrific', 'not fantastic', 'not neato', 'not fantabulous', 'not wowza',
    'not oh-so-not-meh', 'not brilliant', 'not ducky', 'not coolio', 'not incredible',
    'not wonderful', 'not smashing', 'not lovely']

@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>
    <head></head>
    <body>
    <a href="http://localhost:5000/hello">Hello</a>
    </body>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          Want compliment?
          <input type="radio" name="niceormean" value="nice">
           Want diss?
           <input type="radio" name="niceormean" value="mean">
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/diss')
def diss_person():

  player = request.args.get("person")
  niceormean = request.args.get("niceormean")
  compliment = choice(AWESOMENESS)
  insult = choice(DISS)

  if niceormean == "nice":
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head> 
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """ 
  else:
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head> 
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """ 

@app.route('/greet')
def greet_person():
    """Get user by name."""
    
    player = request.args.get("person")
    
    compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head> 
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """ 


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
