from flask import Flask, render_template, request, flash, redirect, url_for

from logging import debug
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:banco123@localhost:5432/task_detailer'

app.config['SECRET_KEY'] = '15(E\xab\x85m\xf3\x8f\xe4q`\x13>\xf9\x14j\xcc\x866}\xbc\r\x03'

db = SQLAlchemy(app)


class Topic(db.Model):
    __tablename__ = 'topics'

    topic_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=255))


class Task(db.Model):
    __tablename__ = 'tasks'

    task_id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.topic_id'))
    description = db.Column(db.String(length=255))

    topic = db.relationship("Topic")


@app.route('/')
def display_topics():
    return render_template('home.html', topics=Topic.query.all())


@app.route('/topic/<topic_id>')
def display_tasks(topic_id):
    return render_template("topic-tasks.html", topic=Topic.query.filter_by(topic_id=topic_id).first(), tasks=Task.query.filter_by(topic_id=topic_id).all())

@app.route('/add/topic', methods=["POST"])
def add_topic():
    if not request.form["topic-title"]:
        flash("Enter a title for your new topic", "tomato")

    else:
        topic = Topic(title=request.form['topic-title'])
        db.session.add(topic)
        db.session.commit()
        flash("Topic Added Successfully", "green")

    return redirect(url_for('display_topics'))


@app.route("/add/task/<topic_id>", methods=["POST"])
def add_task(topic_id):
    if not request.form["task-description"]:
        flash("Enter a description for your new task", "tomato")

    else:
        task = Task(description=request.form["task-description"], topic_id=topic_id)
        db.session.add(task)
        db.session.commit()
        flash("Task Added Successfully", "green")

    return redirect(url_for('display_tasks', topic_id=topic_id))

     
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5533)


