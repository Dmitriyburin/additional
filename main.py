from flask import Flask, render_template, url_for

from data.jobs import Jobs
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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
