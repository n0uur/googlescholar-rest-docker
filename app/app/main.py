"""Google Scholar Rest-API
powered by Flask and Scholarly
"""

import datetime
import json

from scholarly import scholarly, ProxyGenerator
from encoders import ScholarlyEncoder
from flask import Flask

pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)

app = Flask(__name__)


@app.route("/")
def index():
    return {
        "status": "ok",
        "timestamp": datetime.datetime.now().isoformat()
    }


@app.route("/author/name/<name>")
def author_from_name(name):
    search_query = scholarly.search_author(name)
    author = scholarly.fill(next(search_query))
    response = app.response_class(
        response=json.dumps(author, cls=ScholarlyEncoder),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/author/id/<scholar_id>")
def author_from_id(scholar_id):
    author = scholarly.fill(scholarly.search_author_id(scholar_id))
    response = app.response_class(
        response=json.dumps(author, cls=ScholarlyEncoder),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/pubs/<name>")
def pub_from_name(name):
    try:
        query = scholarly.search_pubs(name)
        response = app.response_class(
            response=json.dumps(scholarly.fill(next(query)), cls=ScholarlyEncoder),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception:
        return {
                   'status': 'not found',
                   'message': 'item\'s not found or something went wrong.'
               }, 404


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8080)
