from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, current_user

from forms.user import RegisterForm, LoginForm
from data.jobs import Jobs
from data.users import User
from data import db_session

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def main():
    db_session.global_init("db/lesson.db")
    app.run(debug=True)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    url_style = url_for('static', filename='css/style.css')

    return render_template("index.html", jobs=jobs, url_style=url_style)


@app.route("/add_job")
def add_job():
    db_sess = db_session.create_session()
    url_style = url_for('static', filename='css/style.css')
    # Добавление пользователей
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False

    db_sess.add(job)

    db_sess.commit()
    return render_template("add_job.html", url_style=url_style)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    main()
