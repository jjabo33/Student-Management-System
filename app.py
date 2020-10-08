from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def studentList():
    return render_template('studentsList.html.j2')

@app.route('/assignments')
def assignments():
   return render_template('assignments.html.j2')

@app.route('/addStudent')
def addStudent():
   return render_template('addStudent.html.j2')
