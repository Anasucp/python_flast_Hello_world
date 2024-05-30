# flask library
from flask import Flask


#Creating Instance Flask App
app = Flask(__name__)

#config Flask app
app.config['Debug'] = True


# Routers
@app.route('/')
def home():
	return "Hello World"

#For Running Application
if __name__ == '__main__':
	app.run (debug=True)

