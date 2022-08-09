from flask import Flask, render_template
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


@app.route('/')
def display_topics():
    return render_template('home.html', topics=Topic.query.all())


@app.route('/topic/<topic_id>')
def display_tasks(topic_id):
    return render_template("topic-tasks.html", topic_id=topic_id)

@app.route('/add/topic', methods=["POST"])
def add_topic():
    return "Topic Added Successfully" # add topic functionality


@app.route("/add/task/<topic_id>", methods=["POST"])
def add_task(topic_id):
    return "Task Added Successfully"  # add task functionality

     
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5533)


