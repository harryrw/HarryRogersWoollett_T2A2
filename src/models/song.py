from marshmallow import fields
from init import db, ma

class Song(db.Model):
    __tablename__ = 'songs'

    song_id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String)
    artist = db.Column(db.String)
    genre = db.Column(db.String)
    album = db.Column(db.String)
    song_year = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    song_link = db.Column(db.String)

    playlist_songs = db.relationship('PlaylistSong', back_populates='song')

class SongSchema(ma.Schema):
    class Meta:
        fields = ('song_name', 'artist', 'genre', 'album', 'song_year', 'duration', 'song_link')
        ordered = True