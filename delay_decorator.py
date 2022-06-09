import time


def delay_decorator(function):
	def wrapper_function():
		time.sleep(2)
		# Do something before the function
		function()
		# Do something after the function
	return wrapper_function


@delay_decorator
def say_hello():
	print("Hello !")


def greeting():
	print("Greetings Human !")


say_hello()
# greeting()
