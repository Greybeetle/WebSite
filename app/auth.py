# app/auth.py 用户蓝图
from flask import Blueprint
from flask import url_for, render_template, flash, redirect
from .model import User
from .exts import db
from .forms import RegisterForm, UserLoginForm
from flask_login import login_user, login_required, logout_user

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['POST', 'GET'])
def login():
    login_form = UserLoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        u = User.query.filter_by(username=username).first()
        emsg = None
        if u is None:
            emsg = '用户名不存在'
        elif u.password != password:
            emsg = '密码错误'
        if emsg is None:
            remember = login_form.remember.data
            login_user(u, remember=remember)
            return redirect(url_for('blog.index'))
        flash(emsg)

    return render_template('auth/login.html', form=login_form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    

@bp.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()  # 从request获取表单
    if register_form.validate_on_submit():  # 验证表单完整性
        username = register_form.username.data   # 获取表单中的username
        exists = User.query.filter_by(username=username).first()   # 验证存在性
        if exists:
            emsg = '用户名已存在'
            flash(emsg)  # 提示错误信息
            return render_template('auth/register.html', form=register_form)

        password = register_form.password.data    # 这里后面需要改成加密过程
        u = User(username=username, password=password)  # 创建对象
        db.session.add(u)  # 插入数据
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=register_form)