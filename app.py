from flask import Flask, request, render_template
from main import PatientList

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results_dict = PatientList(query)  # Returns a dictionary
    return render_template('result.html', query=query, results=results_dict)

if __name__ == '__main__':
    app.run(debug=True)