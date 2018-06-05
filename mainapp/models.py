from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  #创建数据库对象，并且初始化app

def init_db(app):
    db.init_app(app)
    Migrate(app,db)

class User(db.Model):  #默认的表名是类名的小写
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20))
    phone = db.Column(db.String(12))

    def __repr__(self):  #重写查询结果
        return '{} {} {}'.format(self.id,self.name,self.phone)

class Music(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))  #歌名
    singer = db.Column(db.String(50))  #歌手
    brand = db.Column(db.String(20))  #所属专辑
    mp3_url = db.Column(db.String(100))  #歌源

    #外键关联
    userid = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User',backref=db.backref('musics',lazy=True))

class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))  #图片名
    url = db.Column(db.String(200))  #图片源

class Collect(db.Model):  #收藏图片
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    img_id = db.Column(db.Integer, db.ForeignKey('img.id'))


