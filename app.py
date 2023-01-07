from flask import Flask, render_template, redirect, request
import lesfonctions, re
name="main"
app = Flask(name)
partage_data=""

@app.route('/arte', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            requestresult=str(request.form)
            if re.search("jour", requestresult)!= None:
                return redirect('/arte/programme_du_jour')
            elif re.search("categories", requestresult)!= None:
                return redirect('/arte/categories')
            else:
                return render_template('index.html')
        return render_template('index.html')
    
    except Exception as error:
        print(error)



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

@app.route('/arte/categories')
def get_arte_categories():
    try:
        return "OK"

    except Exception as error:
        print(error)


if name == 'main':
    app.run()