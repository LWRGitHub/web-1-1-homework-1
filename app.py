
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    """ Tell the use how peguins are cute """
    return 'Penguins are cute!'

@app.route('/favanimal')
def favAnimal():
    """ Tell users favorit animal """
    return '<p>My favorit animal is a monky!</p>'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'<p>Wow, {users_animal} is my favorite animal, too!</p>'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """ Display favorite dessert """
    return f'<p>How did you know I liked {users_dessert}?</p>'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """ Mad lib """
    return f'<p>there was a race & the {noun} {adjective} all the way to the finish line!</p>'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """ Multipy numbers """
    if number1.isdigit() and number2.isdigit():
        return f'{number1} times {number2} is {int(number1) * int(number2)}.'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """ Repeat users word n times """
    if n.isdigit():
        sting = ''
        for x in range(int(n)):
            sting += word + ' '
        return sting
    else:
        return '<p>Invalid input. Please try again by entering a word and a number!</p>'

@app.route('/reverse/<word>')
def reverse(word):
    """ Reverse the letters in the users word """
    string = ''
    i = len(word) - 1
    for x in range(len(word)):
        string += word[i]
        i -= 1 
        
    return f"<p>{string}</p>"

@app.route('/strangecaps/<word>')
def strangecaps(word):
    """ Every other letter in word turns to CAPS """
    string = ''
    for x in range(len(word)):
        if x % 2:
            string += word[x].upper()
        else:
            string += word[x]
    return f"<p>{string}</p>"

@app.route('/dicegame')
def dicegame():
    """ Role the dice, if you get a 6 you win """
    yourNum = random.randint(1, 6)
    if yourNum == 6:
        return f'<p>You rolled a {yourNum}. You won!</p>'
    else:
        return f'<p>You rolled a {yourNum}. You lost!</p>'

@app.route('/triple/<word>')
def triple(word):
    """ write word 3 times """
    return f'<p>{word} {word} {word}</p>'

if __name__ == '__main__':
    app.run(debug=True)


