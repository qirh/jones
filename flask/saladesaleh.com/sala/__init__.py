# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, send_file, send_from_directory
app = Flask(__name__)

@app.errorhandler(404)
def own_404_page(num1=None, num2=None, num3=None, error1=None, error2=None):
    if num1 is None or num2 is None or num3 is None:
        num1 = '4'
        num2 = '0'
        num3 = '4'
    if error1 is None or error2 is None:
        error1 = 'PAGE NOT FOUND'
        error2 = 'The requested page could not be found'

    return render_template('/404.html', title='Saleh', num1 = num1, num2 = num2, num3 = num3, error1 = error1, error2 = error2)

@app.route("/")
@app.route("/en")
@app.route("/en/")
@app.route("/en/index")
@app.route ("/index")
def index():
    return render_template('index.html', title='Saleh')
@app.route("/en/cv")
@app.route ("/cv")
def cv():
    return render_template('cv.html', title='Saleh')
@app.route("/en/graph")
@app.route ("/graph")
def graph():
    return render_template('graph.html', title='Saleh')
@app.route("/en/projects")
@app.route ("/projects")
def projects():
    return render_template('projects.html', title='Saleh')
@app.route("/en/cambridgeart")
@app.route ("/cambridgeart")
def cambridgeart():
    return render_template('proj-cambridgeart.html', title='Saleh')
@app.route("/en/myqueue")
@app.route ("/myqueue")
def myqueue():
    return render_template('proj-myqueue.html', title='Saleh')
@app.route("/en/gameoflife")
@app.route ("/gameoflife")
def gameoflife():
    return render_template('proj-gameoflife.html', title='Saleh')
@app.route("/en/downing")
@app.route ("/downing")
def downing():
    return render_template('proj-downing.html', title='Saleh')
@app.route("/en/texas")
@app.route ("/texas")
def texas():
    return render_template('proj-texas.html', title='Saleh')

@app.route('/en/docs/cv')
@app.route('/docs/cv')
def get_cv():
    return send_from_directory('static/docs/', 'CV_Saleh_Alghusson.pdf', )

@app.route('/en/docs/<path:filename>')
@app.route('/docs/<path:filename>')
def get_pdf(filename=None):
    print("0")
    if filename is not None:
        print("1")
        arr = os.listdir(os.path.join(app.static_folder, 'docs'))
        if filename in arr:
            print("2")
            return send_from_directory('static/docs/', filename)
    print("3")
    return own_404_page(error1='FILE NOT FOUND', error2='The requested file could not be found')


###	Espangol
@app.route("/es")
@app.route("/es/")
@app.route ("/es/index")
def es_index():
    return render_template('/es/index.html', title=u'Sáleh')
@app.route ("/es/cv")
def es_cv():
    return render_template('/es/cv.html', title=u'Sáleh')
@app.route ("/es/graph")
def es_graph():
    return render_template('/es/graph.html', title=u'Sáleh')
@app.route ("/es/projects")
def es_projects():
    return render_template('/es/projects.html', title=u'Sáleh')
@app.route ("/es/cambridgeart")
def es_cambridgeart():
    return render_template('/es/proj-cambridgeart.html', title=u'Sáleh')
@app.route ("/es/myqueue")
def es_myqueue():
    return render_template('/es/proj-myqueue.html', title=u'Sáleh')
@app.route ("/es/gameoflife")
def es_gameoflife():
    return render_template('/es/proj-gameoflife.html', title=u'Sáleh')
@app.route ("/es/downing")
def es_downing():
    return render_template('/es/proj-downing.html', title=u'Sáleh')
@app.route ("/es/texas")
def es_texas():
    return render_template('/es/proj-texas.html', title=u'Sáleh')

###	Arabic
@app.route("/ar")
@app.route("/ar/")
@app.route ("/ar/index")
def ar_index():
    return render_template('/ar/index.html', title=u'صالح')
@app.route ("/ar/cv")
def ar_cv():
    return render_template('/ar/cv.html', title=u'صالح')
@app.route ("/ar/graph")
def ar_graph():
    return render_template('/ar/graph.html', title=u'صالح')
@app.route ("/ar/projects")
def ar_projects():
    return render_template('/ar/projects.html', title=u'صالح')
@app.route ("/ar/cambridgeart")
def ar_cambridgeart():
    return render_template('/ar/proj-cambridgeart.html', title=u'صالح')
@app.route ("/ar/myqueue")
def ar_myqueue():
    return render_template('/ar/proj-myqueue.html', title=u'صالح')
@app.route ("/ar/gameoflife")
def ar_gameoflife():
    return render_template('/ar/proj-gameoflife.html', title=u'صالح')
@app.route ("/ar/downing")
def ar_downing():
    return render_template('/ar/proj-downing.html', title=u'صالح')
@app.route ("/ar/texas")
def ar_texas():
    return render_template('/ar/proj-texas.html', title=u'صالح')

