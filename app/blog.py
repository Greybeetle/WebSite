# app/blog.py 博客蓝图
from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import login_required, current_user
from .forms import PostForm
from .model import Post, db
from bs4 import BeautifulSoup

# 使用/访问博客蓝图
bp = Blueprint('blog', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')
    
   
@bp.route('/detail/<int:id>')
@login_required
def detail(id):   # 查
    post = Post.query.get_or_404(id)
    return render_template('blog/detail.html', post=post)


@bp.route('/showall')
@login_required
def show_all_post():
    posts = Post.query.filter_by(author=current_user).order_by(Post.created.desc())
    if posts is not None:
        return render_template('blog/show_all_post.html', posts=posts)
    return "no post"


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():   # 增
    form = PostForm()  # 获取发布博客的表达
    if form.validate_on_submit():
        post = Post(author=current_user)
        post.title = form.title.data.strip()
        post.body = form.body.data
        post.body_html = request.form['test-editormd-html-code']
        post.summary = form.summary.data.strip()
        if not post.summary:
            bs = BeautifulSoup(post.body_html, 'html.parser')
            if len(bs.get_text()) > 255:
                post.summary = bs.get_text[:255]
            else:
                post.summary = bs.get_text()
        db.session.add(post)
        db.session.commit()

        post = Post.query.filter_by(author=current_user, title=post.title).order_by(Post.created.desc()).first()
        return redirect(url_for('blog.detail', id=post.id))

    return render_template('blog/edit.html', form=form)


@bp.route('/update/<post_id>', methods=['GET', 'POST'])
def update(post_id):   # 改
    post = Post.query.get_or_404(post_id)
    return render_template('blog/update.html', post=post)

    # return post_id


@bp.route('/delete/<int:id>')
def delete(id):   # 删
    return 'delete' + str(id)

