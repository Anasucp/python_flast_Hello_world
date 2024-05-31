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



#Dynamic Routes with Type Converters
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'



#Routes with Multiple HTTP Methods

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Processing login'
    else:
        return 'Login page'


#Catch-All Routes
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath: {subpath}'



if __name__ == '__main__':
	app.run (debug=True)

