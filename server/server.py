from flask import Flask, request, jsonify, redirect, url_for, abort, render_template,  flash
import util

from connexion import App

app = Flask(__name__, template_folder='../client' )
# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'Key'

@app.route('/', methods =['GET'])
def get_suburb_names():
    util.load_saved_artifacts()
    mydict =util.get_suburb_names()
    #response = jsonify({
    #    'suburbs': util.get_suburb_names()
    #})
    #response.headers.add('Access-Control-Allow-Origin','*')
    return render_template('app.html',suburbs= mydict)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/predict_home_price', methods =['POST'])
def predict_home_price():
    error = None
    try:
        if request.method == "POST":
            suburb = request.form['suburbs']
            bedrooms = request.form['uibedrooms']
            bathroom = request.form['uiBathroom']
            distance = request.form['distance']
            car = request.form['uicar']
            sqm = request.form['landsize']
            if sqm is None:
                error = 'Please provide Landsize in Numeric value'

            if suburb is None:
                error = 'Please choose suburb from the list'

            if bedrooms is None:
                error = 'Please select bedroom'

            if bathroom is None:
                error = 'Please select a bathroom'

            if car is None:
                error = 'Please select car port'

            if error is not None:
                predictions = 0.0
            else:
                predictions = util.get_estimated_price(suburb, bedrooms, distance, bathroom, car, sqm)
                subList = util.get_suburb_names()
            return render_template('app.html', result=predictions, sub= suburb, size=sqm, suburbs=subList)
    except Exception as e:
        flash(e)
        return jsonify({'error': 'Missing data!'})

if __name__ == '__main__':
    print("Starting Python Flask Server For Melbourne Home Price Prediction...")
    app.run(debug=True,use_reloader=False)