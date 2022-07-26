from flask import Flask
import random

app = Flask(__name__)

rand_num = random.randint(1, 9)
gif_list = ['https://media.giphy.com/media/xT0xeE8uyMskq0Jg9W/giphy.gif',
            'https://media.giphy.com/media/RtFxzpt8RxzDqCAgLh/giphy.gif',
            'https://media.giphy.com/media/cPKtFMVbJhyhO/giphy.gif',
            'https://media.giphy.com/media/d1E1szXDsHUs3WvK/giphy.gif',
            'https://media.giphy.com/media/JsyTC1TiBDuYpbj6ZL/giphy.gif',
            'https://media.giphy.com/media/l0ExncehJzexFpRHq/giphy.gif',
            'https://media.giphy.com/media/26xBPdoEvUPUHWGE8/giphy.gif']

last_gif = ""

def make_h1(fn):
    def wrapper(**kwargs):
        for key, value in kwargs.items():
            return f'<h1>{fn(value)}</h1>'
    return wrapper

def add_gif(fn):
    def wrapper(*args):
        global last_gif
        new_gif = True
        while new_gif:
            gif = random.choice(gif_list)
            if gif != last_gif:
                new_gif = False
        last_gif = gif
        return f'{fn(args[0])}<br><img src={gif}>'
    return wrapper

@app.route('/')
def guess_number():
    global last_gif
    gif = random.choice(gif_list)
    last_gif = gif

    return f"<h1>Guess a number between 0 and 9</h1><img src={gif}>"

@app.route('/<int:number>')
@make_h1
@add_gif
def number_check(number):
    global rand_num
    if number > rand_num:
        return "Sorry you guessed too high!"
    elif number < rand_num:
        return "Sorry you guessed too low!"
    else:
        return "Congratulations, you guessed the number!"


if __name__ == "__main__":
    app.run(debug=True)
