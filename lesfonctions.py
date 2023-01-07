import requests
import jsonpath_rw_ext as jp 
import re

def collect(url):
    try:
        response = requests.get(url)
    except Exception as error:
        print(error)
    return response.json()

def parse_programme_du_jour(collect_result):
    try:
        items=jp.match("$..items[*]",collect_result)
        parselist=[]
        for elements in items:
            titre=elements.get('title')
            heuredebut=elements.get('beginRounded')
            description=elements.get('description')    
            image=re.split('\'url\': |}',str(elements.get('images')))[1]
            parsedict={"titre":titre,"heuredebut":heuredebut,"description":description,"image":image}
            parselist.append(parsedict)
    except Exception as error:
        print(error)
    return parselist

def generate_table(data):
    table = "<table>"
    for d in data:
        table += "<tr>"
        for key, value in d.items():
            if key == "image":
                table += "<td><img src={}></td>".format(value)
            else:
                table += "<td>{}</td>".format(value)
        table += "</tr>"
    table += "</table>"
    return table