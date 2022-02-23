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


if __name__ == '__main__':
    main()
