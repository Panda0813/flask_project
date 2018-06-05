from flask import Flask
from flask_bootstrap import Bootstrap
from mainapp import views, settings, models


def create_app():
    app = Flask(__name__)

    #配置
    app.env = 'development'
    app.config.from_object(settings.Config)

    #初始化
    views.init_blue(app)
    Bootstrap(app)  #初始化样式
    models.init_db(app)  #初始化数据库

    return app