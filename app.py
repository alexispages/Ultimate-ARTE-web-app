from flask import Flask, jsonify, render_template, redirect, request
import lesfonctions
import re

app = Flask(__name__)
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
    list_categorie_parse_result=[]
    list_sans_doublons_categories=[]
    try:
        url = 'https://api.arte.tv/api/player/v2/playlist/fr/LIVE?'
        response=lesfonctions.collect(url)
        parse_result=lesfonctions.parse_categorie(response)
        global partage_data
        partage_data=parse_result

        for element in parse_result:
            list_categorie_parse_result.append(element['categorie'])
        list_sans_doublons_categories=list(set(list_categorie_parse_result))
        return render_template("categories.html",data=list_sans_doublons_categories )

    except Exception as error:
        print(error)

if __name__ == '__main__':
    app.run(debug=True)