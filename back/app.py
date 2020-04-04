from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from api.api_biedronka import api_biedronka
from api.api_user import api_user
from config import Config
from mockup.event_prediction import predictions
from model.biedronka import setup_biedronka_db
from model.user import setup_user_db, setup_apikey_db

app = Flask(__name__)
app_session = Session()
app.config.from_object(Config)
db = SQLAlchemy(app)

app.config["biedronka.db"] = setup_biedronka_db(db)
app.config["user.db"] = setup_user_db(db)
app.config["apikey.db"] = setup_apikey_db(db)

app.register_blueprint(predictions)
app.register_blueprint(api_biedronka)
app.register_blueprint(api_user)

migrate = Migrate(app, db)
db.create_all()

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

app_session.init_app(app)


@app.route('/api/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
