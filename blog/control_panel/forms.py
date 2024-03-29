from flask.ext.wtf import Form
from wtforms import (StringField,
                     PasswordField,
                     BooleanField,
                     SubmitField,
                     TextAreaField
                     )
from wtforms.validators import (Required,
                                Length,
                                Email
                                )


class SetupForm(Form):
    blog_name = StringField("Blog Name", validators=[Required()])
    submit = SubmitField("Finish!")


class LoginForm(Form):
    email = StringField("Email", validators=[Required(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[Required()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("Login")


class NewPostForm(Form):
    title = StringField("Title", validators=[Required()])
    body = TextAreaField("Body")
    draft = SubmitField("Save as Draft")
    post = SubmitField("Post")



