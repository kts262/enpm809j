from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Poppy'}
	return render_template('index.html', title='Home', user=user)

@app.route('/about')
def about():
	user = {'username': 'Poppy'}
	return render_template('about.html', title='About', user=user)

@app.route('/leadership')
def leadership():
	return render_template('leadership.html', title='Leadership' )

@app.route('/videos')
def videos():
	return render_template('videos.html', title='Videos', )

@app.route('/buy')
def buy():
	return render_template('buy.html', title='Buy Video', )
