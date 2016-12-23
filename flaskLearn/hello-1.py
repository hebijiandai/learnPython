from flask import Flask,render_template
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app=Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'

# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello,World:Come from {0}<h1>'.format(name)

# @app.route('/')
# def index():
#     user_agent=request.headers.get('User-Agent')
#     return '<p>Your Browser is {0} </p>'.format(user_agent)

# @app.route('/')
# def index():
#     return '<h1>Bad Ruquest</h1>',400

# @app.route('/')
# def index():
#     response=make_response('<h1>This document carries a cookie!</h1>')
#     response.set_cookie('answer','42')
#     return response

# @app.route('/')
# def index():
#     return redirect('https://www.google.com')

# @app.route('/user/<id>')
# def get_user(id):
#     user=load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello,{0}'.format(user.name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

if __name__=='__main__':
    app.run(debug=True)