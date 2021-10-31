import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    data = []
    return render_template('index.html', data=json.dumps(data))

if __name__ == '__main__':
   app.run()