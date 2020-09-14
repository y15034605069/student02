from flask import  Flask,render_template,Response
app = Flask(__name__)

class Config(object):
    DEBUG = True

app.config.from_object(Config)

@app.route('/index')
def index():
    return Response('哈哈哈哈')


if __name__ == '__main__':
    app.run()