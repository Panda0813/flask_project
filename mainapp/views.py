from flask import Blueprint, Flask, render_template, request, session, redirect, url_for

from mainapp.models import User, Music, Img, Collect

blue = Blueprint('main',__name__)

def init_blue(app:Flask):
    app.register_blueprint(blue)


@blue.route('/')
def home():
    p = User.query.paginate(1,3)
    return render_template('home.html',title='主页',pagination = p)

@blue.route('/nextuser/')
def nextUser():
    page = int(request.args.get('page'))
    p = User.query.paginate(page,3)
    return render_template('home.html',title='主页',pagination = p)


@blue.route('/login/',methods=('GET','POST'))
def login():
    if request.method == 'GET':
        return render_template('login.html',title='登录界面')
    else:
        name = request.form.get('name')
        user = User.query.filter(User.name == name).first()
        session['login_name'] = user.name
        session['login_id'] = user.id

        return redirect(url_for('main.home'))

@blue.route('/logout/')
def logout():  #退出登录
    session.pop('login_name')
    session.pop('login_id')
    return redirect(url_for('main.home'))

#根据登录的用户id把他的
@blue.route('/musiclist/')
def musiclist():
    userid = session.get('login_id')
    user = User.query.get(userid)
    musics = user.musics
    return render_template('musiclist.html',title='我的音乐',musics=musics)

@blue.route('/playmusic/<int:musicid>/')
def playmusic(musicid):
    music = Music.query.get(musicid)
    user_id = music.userid  #等到用户id,也可以从session中取
    # 拿出所有照片，播放音乐时可以循环
    imgs = Img.query.join(Collect).filter(Collect.user_id == user_id).all()
    return render_template('playmusic.html',music=music,imgs=imgs)