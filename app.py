from flask import Flask, jsonify
import requests
name="main"
app = Flask(name)

@app.route('/arte')
def get_arte_data():

    url = 'https://api.arte.tv/api/player/v2/playlist/fr/LIVE?'
    response = requests.get(url)
    return jsonify(response.json())

if name == 'main':
    app.run()