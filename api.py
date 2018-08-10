import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {
        "node_type": "node",
        "nodeResponse": {
            "type": "image",
            "response": "https://www.70millionthailand.org/api/jsonShowImageByType/id/62106/attribute/path_img"
        }
    }
]


@app.route('/home', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/image/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/image', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    # results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    # for book in books:
    #     if book['id'] == id:
    #         results.append(book)

    results = [
                {
                    "node_type": "node",
                    "nodeResponse": {
                        "type": "image",
                        "response": "https://www.70millionthailand.org/api/jsonShowImageByType/id/"+str(id)+"/attribute/path_img"
                    }
                }
            ]

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run()