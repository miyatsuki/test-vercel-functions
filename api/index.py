from flask import Flask, Response
app = Flask(__name__)

@app.route('/api/test1')
def catch1(path):
    return Response("<h1>Flask</h1><p>You visited:test1", mimetype="text/html")

@app.route('/api/test2')
def catch2(path):
    return Response("<h1>Flask</h1><p>You visited:test2", mimetype="text/html")

@app.route('/api/test3')
def catch3(path):
    return Response("<h1>Flask</h1><p>You visited:test3", mimetype="text/html")

@app.route('/api/test4')
def catch4(path):
    return Response("<h1>Flask</h1><p>You visited:test4", mimetype="text/html")