import csv

from flask import Flask
from flask import Response, request, make_response
app = Flask(__name__)

@app.route('/')
def do_index():
    return 'This is the index page'

@app.route('/chunk', methods=['POST'])
def do_chunk():
    if request.method == 'POST':
        raw_data = request.get_data(as_text=True).split("\n")
        if request.headers.get('md5'):
            file_name = request.headers['md5']
        with open(file_name, 'w') as f:
            writer = csv.writer(f, delimiter=',')
            for line in raw_data:
                writer.writerow(line.split(","))
        response = make_response("data is stored into local csv successfully.")
        return response

app.run(port=5050)
