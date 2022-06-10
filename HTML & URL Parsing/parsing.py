from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
	return "<h1 style='text-align': center>Hello, World!</h1>" \
	       "<p>Lorem Ipsum ...</p>" \
	       "<img src='https://media.giphy.com/media/FWAcpJsFT9mvrv0e7a/giphy.gif'>"


@app.route("/bye")
def bye():
	return "Bye !"


@app.route("/username/<name>")
def greet(name):
	return f"Hello {name}"


if __name__ == "__main__":
	app.run(debug=True)
