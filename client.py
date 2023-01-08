from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
  # Charger les données JSON à partir du fichier data.json
  with open('data.json', 'r') as f:
    data = json.loads(f.read())
  # Passer les données à la template HTML
  return render_template('client.html', data=data)
  


if __name__ == '__main__':
    app.run(host='localhost', port=3000)
