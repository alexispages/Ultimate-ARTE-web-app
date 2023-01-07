from flask import Flask, jsonify
import lesfonctions
name="main"
app = Flask(name)

@app.route('/arte/programme_du_jour')
def get_arte_programme_du_jour():

    try:
        url = 'https://api.arte.tv/api/player/v2/playlist/fr/LIVE?'
        response=lesfonctions.collect(url)

        return response

    except Exception as error:
        print(error)


if name == 'main':
    app.run()