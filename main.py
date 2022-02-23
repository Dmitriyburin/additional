import datetime

from flask import Flask, render_template, redirect

from forms.user import RegisterForm, LoginForm
from data.jobs import Jobs
from data.users import User
from data import db_session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/lesson.db")
    app.run()


USERS = [
    {
        "surname": "Scott",
        "name": "Ridley",
        "age": 21,
        "position": "captain",
        "speciality": "research engineer",
        "address": "module_1",
        "email": "scott_chief@mars.org",
        'hashed_password': generate_password_hash('password1'),
    },
    {
        "surname": "Кубышкина",
        "name": "Дарья",
        "age": 61,
        "position": "colonist",
        "speciality": "labor force",
        "address": "module_2",
        "email": "darya1960@gmail.com",
        'hashed_password': generate_password_hash('password2'),
    },
    {
        "surname": "Завьялова",
        "name": "Жанна",
        "age": 39,
        "position": "colonist",
        "speciality": "labor force",
        "address": "module_3",
        "email": "janna.zavyalova@hotmail.com",
        'hashed_password': generate_password_hash('password3'),
    },
    {
        "surname": "Бухаров",
        "name": "Артем",
        "age": 59,
        "position": "colonist",
        "speciality": "labor force",
        "address": "module_4",
        "email": "artem99@hotmail.com",
        'hashed_password': generate_password_hash('password4'),
    },
    {
        "surname": "Яблоновская",
        "name": "Елизавета",
        "age": 31,
        "position": "colonist",
        "speciality": "labor force",
        "address": "module_5",
        "email": "elizaveta26091990@yandex.ru",
        'hashed_password': generate_password_hash('password5'),
    },
]


@app.route("/add_user")
def add_user():
    db_sess = db_session.create_session()

    # Добавление пользователей
    for usr in USERS:
        user = User()
        user.surname = usr['surname']
        user.name = usr['name']
        user.age = usr['age']
        user.position = usr["position"]
        user.speciality = usr['speciality']
        user.address = usr['address']
        user.email = usr['email']
        user.hashed_password = usr['hashed_password']

        db_sess.add(user)

    db_sess.commit()
    return "Данные добавлены!"


@app.route("/add_job")
def add_data():
    db_sess = db_session.create_session()

    # Добавление пользователей
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False

    db_sess.add(job)

    db_sess.commit()
    return "Данные добавлены!"


if __name__ == '__main__':
    main()
