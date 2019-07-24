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

DISSES = ['dumb', 'lame', 'annoying', 'boring', 'stupid']


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
    <a href="/hello">This is a link to Hello.</a></html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person"><br>
          
          <input type="radio" name="compliment" value="{AWESOMENESS[0]}">{AWESOMENESS[0]}<br>
          <input type="radio" name="compliment" value="{AWESOMENESS[1]}">{AWESOMENESS[1]}<br>
          <input type="radio" name="compliment" value="{AWESOMENESS[2]}">{AWESOMENESS[2]}<br>
          <input type="radio" name="compliment" value="{AWESOMENESS[3]}">{AWESOMENESS[3]}<br>
          <input type="radio" name="compliment" value="{AWESOMENESS[4]}">{AWESOMENESS[4]}<br>
          <input type="radio" name="compliment" value="{AWESOMENESS[5]}">{AWESOMENESS[5]}<br>
          <input type="radio" name="compliment" value="{AWESOMENESS[6]}">{AWESOMENESS[6]}<br>
          <input type="radio" name="compliment" value="{AWESOMENESS[7]}">{AWESOMENESS[7]}<br>
          <input type="radio" name="compliment" value="{AWESOMENESS[8]}">{AWESOMENESS[8]}<br>
          <input type="radio" name="compliment" value="{AWESOMENESS[9]}">{AWESOMENESS[9]}<br>
          <input type="radio" name="compliment" value="{AWESOMENESS[10]}">{AWESOMENESS[10]}<br>
          <input type="radio" name="compliment" value="{AWESOMENESS[11]}">{AWESOMENESS[11]}<br>
          <input type="radio" name="compliment" value="{AWESOMENESS[12]}">{AWESOMENESS[12]}<br>
          <input type="radio" name="compliment" value="{AWESOMENESS[13]}">{AWESOMENESS[13]}<br>

          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route("/diss")
def diss_person():
  """Disses user by name"""

  player = request.args.get("person")

  diss = choice(DISSES)

  return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, diss)




if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
