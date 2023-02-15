from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
  user_name = request.args.get("userName", "unknown")
  return render_template('main.html', user=user_name) 