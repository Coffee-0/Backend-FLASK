import random
from flask import Flask

RANDOM_NUMBER = random.randint(0, 9)

app = Flask(__name__)


@app.route("/")
def home():
	return "<h1> Guess a number between 0 and 9 </h1>" \
	       "<img src='https://media.giphy.com/media/3jN3GziOKUEmI/giphy.gif' alt-text='confused doggo'>"


@app.route("/url/<number>")
def guess(number):
	if int(number) == RANDOM_NUMBER:
		return "<img src='https://media.giphy.com/media/l1J3pZOnBQ1qeBwZ2/giphy.gif'>" \
		       "<h1>YAY! You found meeeeeeeeeeee 😀</h1>"

	elif int(number) > RANDOM_NUMBER:
		return "<img src='https://media.giphy.com/media/DNe4LKL6iwZ2goCSx6/giphy.gif'>" \
		       "<h2>🥲 Number TOO High</h2>" \
		       "<h3>Try Again ...</h3>"

	elif int(number) < RANDOM_NUMBER:
		return "<img src='https://media.giphy.com/media/DNe4LKL6iwZ2goCSx6/giphy.gif'>" \
		       "<h2>🥲 Number TOO Low</h2>" \
		       "<h3>Try Again ...</h3>"


if __name__ == "__main__":
	app.run(debug=True)
