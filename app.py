
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
    return 'Penguins are cute!'

@app.route('/favanimal')
def favAnimal():
    return 'My favorit animal is a monky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f'there was a race & the {noun} {adjective} all the way to the finish line!'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        return f'{number1} times {number2} is {int(number1) * int(number2)}.'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    if n.isdigit():
        sting = ''
        for x in range(int(n)):
            sting += word + ' '
        return sting
    else:
        return 'Invalid input. Please try again by entering a word and a number!'

@app.route('/reverse/<word>')
def reverse(word):
    string = ''
    i = len(word) - 1
    for x in range(len(word)):
        string += word[i]
        i -= 1 
        
    return string

@app.route('/strangecaps/<word>')
def strangecaps(word):
    string = ''
    for x in range(len(word)):
        if x % 2:
            string += word[x].upper()
        else:
            string += word[x]
    return string

@app.route('/dicegame')
def dicegame():
    yourNum = random.randint(1, 6)
    if yourNum == 6:
        return f'You rolled a {yourNum}. You won!'
    else:
        return f'You rolled a {yourNum}. You lost!'


if __name__ == '__main__':
    app.run(debug=True)
