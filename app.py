from flask import Flask, render_template, redirect, request
import lesfonctions, re
name="main"
app = Flask(name)

@app.route('/arte')
def get_arte_data():
    #url = 'https://api.arte.tv/api/opa/v3/works?fields=id,title,shortDescription,previewPictures'
    url = 'https://api.arte.tv/api/player/v2/playlist/fr/LIVE?'
    response = requests.get(url)
    return jsonify(response.json())

if name == 'main':
    app.run()