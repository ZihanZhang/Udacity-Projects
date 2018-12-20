from flask import Flask, render_template, request, Response, redirect, url_for, session, abort
from application import db
from application.models import User
from application.forms import EnterDBInfo, LoginForm
from flask.ext.login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user 

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2' 

# flask-login
login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = "login"  

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    # form1 = EnterDBInfo(request.form) 
    
    # if request.method == 'POST' and form1.validate():
    #     data_entered = User(username=form1.username.data, password=form1.password.data)
    #     try:     
    #         db.session.add(data_entered)
    #         db.session.commit()        
    #         db.session.close()
    #     except:
    #         db.session.rollback()
    #     return render_template('thanks.html', username=form1.username.data)
        
    # return render_template('index.html', form1=form1)

    return Response("Hello")

if __name__ == '__main__':
    application.run(host='0.0.0.0')

class User1(UserMixin):

    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_secret"
        
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

users = [User1(id) for id in range(1, 21)]

@application.route('/register', methods=['GET', 'POST'])
def register():
    form1 = EnterDBInfo(request.form) 
    
    if request.method == 'POST' and form1.validate():
        data_entered = User(username=form1.username.data, password=form1.password.data)
        try:     
            db.session.add(data_entered)
            db.session.commit()        
            db.session.close()
        except:
            db.session.rollback()
        return Response('''Registration Success
                            <div>
                                <h3>Log In</h3>
                                <form method="GET" action="/login">
                                    <button type="submit">Log In</button>
                                </form>
                            </div>''')
        
    return render_template('register.html', form1=form1)

@application.route('/login', methods=['GET', 'POST'])
def login():
    form2 = LoginForm(request.form)

    if request.method == 'POST':
        fusername=form2.username.data        
        fpassword=form2.password.data       
        if User.query.filter(User.username==fusername, User.password==fpassword).first():
            login_user(User1(User.query.filter(User.username==fusername, User.password==fpassword).first().id))
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return render_template('login.html', form2=form2)

# somewhere to logout
@application.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User1(userid)