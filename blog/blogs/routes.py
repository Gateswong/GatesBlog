from flask import (render_template,
                   redirect,
                   url_for,
                   request
                   )
from sqlalchemy.orm.exc import (
    NoResultFound,
)

from . import blogs
from ..models.post import Post
from ..utils import (load_page_meta,
                     NotSetup
                     )


@blogs.route("/")
def home():
    posts = Post.query_page_of_posts()
    return render_template("blogs/index.html",
                           posts=posts,
                           page_num=1,
                           page_total=Post.total_pages())


@blogs.route("/terminal")
def dev_terminal():
    raise


@blogs.route("/posts", methods=["GET"])
def post_list():
    # Get Page Num from query string
    try:
        page_num = int(request.args.get("page", 1))
    except ValueError:
        page_num = 1

    # Get tags and category filter
    tags = request.args.get("tags", None)
    if tags: tags = tags.split(",")
    category = request.args.get("category", "")

    posts = Post.query_page_of_posts(skip=(page_num - 1) * 25,
                                     limit=25,
                                     tags=tags,
                                     category=category)

    return render_template("blogs/index.html",
                           posts=posts,
                           page_num=page_num,
                           page_total=Post.total_pages())


@blogs.route("/post/<int:post_id>", methods=["GET"])
def post(post_id):
    is_raw = request.args.get("raw", 0) == 1

    try:
        post = Post.query_one_post(post_id)
    except NoResultFound:
        return "Not Found", 404

    if is_raw:
        post_body = post.content
    else:
        post_body = post.content

    return render_template("blogs/post.html",
                           post=post,
                           post_body=post_body)

