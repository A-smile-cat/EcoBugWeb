import os
from flask import Flask, request, send_from_directory, render_template


app = Flask(__name__)

'''
app.debug=True
app.config.update(DEBUG=True)
app.config.from_object(config)
app.config.from_pyfile('config.cnf', silent=True)
'''
#app.static_folder = 'static'
#app.static_url_path = '/static'

#app.config['UPLOAD_FOLDER'] = 'demo/src'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/insect')
def insect():
    return render_template('insect.html')
@app.route('/datashow')
def datashow():
    return render_template('datashow.html')
@app.route('/app-profile')
def app_profile():
    return render_template('app-profile.html')
@app.route('/app-widget-card')
def app_widget_card():
    return render_template('app-widget-card.html')
@app.route('/dashboard1')
def dashboard1():
    return render_template('dashboard1.html')
@app.route('/dashboard2')
def dashboard2():
    return '网站正在加紧建设中...'
@app.route('/chart')
def chart():
    return render_template('chart.html')
@app.route('/table')
def table():
    return render_template('table.html')
@app.route('/datamap')
def datamap():
    return render_template('datamap.html')
@app.route('/images')
def images():
    return render_template('images.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)    #host='0.0.0.0'


