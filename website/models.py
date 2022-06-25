from datetime import datetime
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Wallpaper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallpaperTitle = db.Column(db.String(255))
    wallpaperSubTitle = db.Column(db.String(255))
    tipeWallpaper = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now())
    downloads = db.Column(db.Integer, default = 0)
    fileWallpaper = db.Column(db.String(255))
    dataWallpaper = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(2000))
    username = db.Column(db.String(150))
    fullname = db.Column(db.String(150))
    gender = db.Column(db.String(50))
    role = db.Column(db.String(50))
    fileProfile = db.Column(db.String(255))
    dataProfile = db.Column(db.LargeBinary)
    wallpaper = db.relationship('Wallpaper')
    
    
    