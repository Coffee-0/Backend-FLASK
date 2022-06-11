from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
def welcome():
	return "Hello!"


@app.route("/guess/<name>")
def guess(name):

	age_url = f"https://api.agify.io?name={name}"
	age_response = requests.get(age_url)
	age_data = age_response.json()
	age = age_data["age"]

	gender_url = f"https://api.genderize.io?name={name}"
	gender_response = requests.get(gender_url)
	gender_data = gender_response.json()
	gender = gender_data["gender"]

	return render_template("guess.html", user_name=name, gender=gender, age=age)


if __name__ == "__main__":
	app.run(debug=True)
