import praw
from flask import Flask, render_template

# SETUP
app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR SECRET KEY'

# REDDIT CLIENT
reddit = praw.Reddit(client_id='YOUR CLIENT ID', client_secret='YOUR CLIENT SECRET', user_agent='APP NAME')


def get_posts():
    posts = reddit.subreddit('spaceporn').new(limit=10)
    return posts


@app.route('/')
def home():
    posts = get_posts()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run()