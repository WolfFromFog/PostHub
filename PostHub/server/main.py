import json
import base64

from flask import Flask, render_template, request

from DataBase.posts import CFDataBasePosts
from DataBase.comments import CFDataBaseComments
from DataBase.categories import CFDataBaseCategories

app = Flask(__name__, template_folder="Views", static_folder="Views")
db_posts = CFDataBasePosts()
db_comments = CFDataBaseComments()
db_categories = CFDataBaseCategories()


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    posts = {
        "posts": db_posts.getPosts(),
        "categories": db_categories.getCategories()
    }
    return render_template('index.html', posts=json.dumps(posts))


@app.route('/createPost', methods=['POST'])
def create_post():
    image = request.files['image']
    image_data = image.read()
    image_base64 = "data:image/jpeg;base64," + base64.b64encode(image_data).decode('utf-8')

    db_posts.addPost({
        'user_nickname': request.form.get('username'),
        'header': request.form.get('header'),
        'main_text': request.form.get('text'),
        'image': image_base64,
        'date': request.form.get('date'),
        'categories': request.form.get('categories')
    })

    return { "message": "OK" }


@app.route('/post/<int:post_id>', methods=['GET'])
def page(post_id=-1):
    post = {
        "post": db_posts.getPost(post_id),
        "comments": db_comments.getComments(post_id),
        "categories": db_categories.getCategories()
    }
    return render_template('page.html', post=json.dumps(post))


@app.route('/create_article', methods=['GET'])
def create_article():
    return render_template('create_article.html', categories=json.dumps(db_categories.getCategories()))


@app.route('/sendComment', methods=['POST'])
def send_post():
    return db_comments.addComment({
        'post_id': request.form.get('post_id'),
        'nickname': request.form.get('username'),
        'text': request.form.get('main_text'),
        'date': request.form.get('date')
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0')
