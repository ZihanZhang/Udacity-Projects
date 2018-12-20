from flask.ext.wtf import Form
from wtforms import TextField, validators

class EnterDBInfo(Form):
    username = TextField(label='Username', description="db_enter", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])   
    password = TextField(label='Password', description="password", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])

class LoginForm(Form):
    username = TextField(label='Username', description="db_enter", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])   
    password = TextField(label='Password', description="password", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])
