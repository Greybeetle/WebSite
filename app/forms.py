from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length


class RegisterForm(FlaskForm):
    """
    用户注册表单
    """
    username = StringField(
        label='用户名',
        validators=[DataRequired(message='用户名不能为空！'),
                    Length(min=3, max=25, message='用户名长度在3-25个字符之间！')]
    )
    password = PasswordField(
        label='密码',
        validators=[DataRequired(message='密码不能为空！'),
                    Length(min=6, max=25, message='密码需要6-25个字符！')]
    )
    confirm = PasswordField(
        label='确认密码',
        validators=[EqualTo('password', message='两次密码不一致')]
    )
    submit = SubmitField(label='注册')


class UserLoginForm(FlaskForm):
    """
    用户登录表单
    """
    username = StringField(
        label='用户名',
        validators=[DataRequired(message='用户名不能为空！')]
    )
    password = PasswordField(
        label='密码',
        validators=[DataRequired(message='密码不能为空！')]
    )
    remember = BooleanField(label='记住我')
    submit = SubmitField(label='登录')


class PostForm(FlaskForm):
    """
    发布博客表单
    """
    title = StringField('文章标题', [DataRequired(), Length(min=6, max=255)])
    summary = TextAreaField('文章摘要')
    body = TextAreaField('文章内容', [DataRequired()])
    submit = SubmitField(label='发布')

