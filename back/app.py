from flask import Flask

from mockup.event_prediction import predictions

app = Flask(__name__)
app.register_blueprint(predictions)

@app.route('/api/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')