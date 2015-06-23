from arrow import arrow

from .. import db


__all__ = ["Post", "Tag", "Category"]


association_table_for_posts_and_tags = db.Table(
    "association_posts_tags",
    db.Model.metadata,
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"))
)


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)

    deleted = db.Column(db.Boolean, default=False)

    category = db.Column(db.Integer, db.ForeignKey("categories.id"))
    tags = db.relationship("Tag",
                           secondary=association_table_for_posts_and_tags,
                           backref="posts")

    time_created = db.Column(db.DateTime(timezone=True), default=arrow.Arrow.now().datetime)
    time_modified = db.Column(db.DateTime(timezone=True), default=arrow.Arrow.now().datetime)

    @classmethod
    def query_page_of_posts(cls, limit=25, skip=0, tags=None, category=None):
        q = db.session.query(Post).filter(Post.deleted == False)

        if category:
            q = q.filter(Post.category == category)

        if tags:
            q = q.filter(Post.tags.any(Tag.id.in_(tags)))

        q = q.slice(skip, skip + limit)

        return q.all()

    @classmethod
    def query_one_post(cls, post_id):
        q = db.session.query(Post).filter(Post.deleted == False, Post.id == post_id).one()

        return q

    @classmethod
    def new_post(cls, title, content, **kwargs):
        post = Post(title=title,
                    content=content)
        db.session.add(post)

        db.session.commit()

    @classmethod
    def total_pages(cls, posts_per_page=25):
        q = db.session.query(Post).filter(Post.deleted == False)

        return q.count() / posts_per_page + 1


class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)


