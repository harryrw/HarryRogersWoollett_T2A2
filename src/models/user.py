from marshmallow import fields
from init import db, ma


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    playlists = db.relationship('Playlist', back_populates='user', cascade='all, delete')
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete')

class UserSchema(ma.Schema):
    playlists = fields.List(fields.Nested('PlaylistSchema'))
    comments = fields.List(fields.Nested('CommentSchema'))

    class Meta:
        fields = ('user_id', 'first_name', 'last_name', 'email', 'password', 'is_admin', 'playlists', 'comments')
        ordered = True