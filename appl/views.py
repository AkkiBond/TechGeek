from flask import render_template, url_for, flash, redirect, request, abort
from appl import app, db, bcrypt
from appl.forms import UserForm, UserLogin, BlogForm, CommentForm
from appl.models import User, Blog, Comment
from flask_login import login_user, current_user, logout_user, login_required
import werkzeug


# route for home page
@app.route("/")
@app.route("/home")
def home():
    posts = Blog.query.all()
    return render_template('home.html', posts=posts)


# route for register page
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data,
                    password=hashed_password, username=form.username.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Login !', 'success')
        return redirect(url_for('login'))
    return render_template('user_reg.html', title='Register', form=form)


# route for login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user)
            redirect(url_for('home'))
        else:
            flash('Please check email and password', 'danger')
    return render_template('user_login.html', title='Login', form=form)


# route for logout
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


# route for blog creation
@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = BlogForm()
    if form.validate_on_submit():
        post = Blog(title=form.title.data, intro=form.intro.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


# route for blog
@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
    post = Blog.query.get_or_404(post_id)
    comments = Comment.query.filter_by(poston=post_id).all()
    form = CommentForm()
    if form.validate_on_submit():
        comm = Comment(content=form.comment.data,
                       name=current_user.username, poston=post_id)
        db.session.add(comm)
        db.session.commit()
        return redirect(url_for('post', post_id=post_id))
    return render_template('post.html', title=post.title,
                           post=post, masti=comments, form=form)


# route for blog updation
@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Blog.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = BlogForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.intro = form.intro.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.intro.data = post.intro
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


# route for deletion of blog
@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Blog.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))


# error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# error handling
@app.errorhandler(werkzeug.routing.BuildError)
def handle_bad_request(e):
    return render_template('403.html'), 403


# note that we set the 500 status explicitly
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500