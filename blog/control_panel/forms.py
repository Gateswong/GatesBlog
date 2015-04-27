from flask.ext.wtf import Form
from wtforms import (StringField,
                     PasswordField,
                     BooleanField,
                     SubmitField
                     )
from wtforms.validators import (Required,
                                Length,
                                Email
                                )


class SetupForm(Form):
    blog_name = StringField("Blog Name", validators=[Required()])
    submit = SubmitField("Finish!")
