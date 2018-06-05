from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import pymysql
from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.env = 'development'
app.debug = True

# SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'


SECRET_KEY = 'adadgf33r23dfv332'


app.config.from_object(__name__)  #从当前脚本中加载相关配置

#创建bootstrap对象
Bootstrap(app)

#创建debug调试工作台
DebugToolbarExtension(app)

#创建cache缓存对象
cache = Cache(app,config={'CACHE_TYPE':'simple'})



@app.route('/')
@cache.cached(timeout=30)
def home():
    print('index 查询所有')
    return render_template('home.html',title='主页')


if __name__ == '__main__':
    app.run(debug=True)
