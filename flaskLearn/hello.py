from flask.ext.bootstrap import Bootstrap
from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell
from flask.ext.mail import Mail, Message
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
manager = Manager(app)

# 添加命令

# 配置邮件设置，初始化
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin<you@gmail.com']
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
mail = Mail(app)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
    sender = app.config['FLASKY_MAIL_SENDER'], recipients = [to])
    msg.body=render_template(template + '.txt', **kwargs)
    msg.html=render_template(template + '.html', **kwargs)
    mail.send(msg)

def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role)
manager.add_command('shell', Shell(make_context=make_shell_context))

# 初始化sqlalchemy
app.config['SECRET_KEY']='Hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI']=
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)
migrate=Migrate(app, db)
manager.add_command('db', MigrateCommand)


class NameForm(Form):
    name=StringField('What is your name?', validators = [DataRequired()])
    submit=SubmitField('Submit')


class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(64), unique = True)
    catname=db.Column(db.String(64), unique = True)
    users=db.relationship('User', backref = 'role')

    def __repr__(self):
        return '<Role {0}>'.format(self.name)


class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer, primary_key = True)
    username=db.Column(db.String(64), unique = True, index = True)
    role_id=db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User {0}>'.format(self.name)

# db.drop_all()
# db.create_all()
#
# admin_role = Role(name="Admin")
# mod_role = Role(name="Moderator")
# user_role = Role(name='User')
# user_john = User(username='john', role=admin_role)
# user_susan = User(username='susan', role=mod_role)
# user_david = User(username='david', role=user_role)
#
# db.session.add(admin_role)
# db.session.add(mod_role)
# db.session.add(user_role)
# db.session.add(user_john)
# db.session.add(user_susan)
# db.session.add(user_david)
#
#
#
# db.session.commit()
#
# print(admin_role.id)
# print(mod_role.id)
# print(user_role.id)
#
# admin_role.name='Administrator'
# db.session.add(admin_role)
# db.session.commit()
# print(admin_role.name)
#
# db.session.delete(mod_role)
# db.session.commit()
#
# print(Role.query.all())
#
# print(Role.query.filter_by(name=admin_role.name).all())
#
# print(str(Role.query.filter_by(name=admin_role.name).first()))


@app.route("/", methods = ['GET', 'POST'])
def index():
    form=NameForm()
    if form.validate_on_submit():
        role=Role.query.filter_by(name = form.name.data).first()
        if role is None:
            role=Role(name = form.name.data)
            db.session.add(role)
            session['known']=False
        else:
            session['known']=True
        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('index'))
    return render_template('index.html', form = form, name = session.get('name'), known = session.get('known', False))

# 发邮件的窗体代码
# @app.route('/', methods = ['GET', 'POST'])
# def index():
#     form=NameForm()
#     if form.validate_on_submit():
#         user=User.query.filter_by(username = form.name.data).first()
#         if user is None:
#             user=User(username = form.name.data)
#             db.session.add(user)
#             session['known']=False
#             if app.config['FLASKY_ADMIN']:
#                 send_email(app.config['FLASKY_ADMIN'], 'New User',
#                 'mail/new_user', user = user)
#         else:
#             session['known']=True
#         session['name']=form.name.data
#         form.name.data=''
#         return redirect(url_for('index'))
#     return render_template('index.html', form = form, name = session.get('name'), known = session.get('known', False))

@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name = name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    # app.run(debug=True)
    manager.run()
