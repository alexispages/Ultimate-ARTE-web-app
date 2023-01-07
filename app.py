from flask import Flask, render_template
import lesfonctions
name="main"
app = Flask(name)

@app.route('/arte/programme_du_jour')
def get_arte_programme_du_jour():

    try:
        url = 'https://api.arte.tv/api/player/v2/playlist/fr/LIVE?'
        response=lesfonctions.collect(url)
        parse_result=lesfonctions.parse_programme_du_jour(response)
        table=lesfonctions.generate_table(parse_result)
        return render_template("programmedujour.html", table=table)

    except Exception as error:
        print(error)


if name == 'main':
    app.run()