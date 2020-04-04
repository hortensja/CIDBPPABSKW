import uuid


def setup_user_db(db):
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64), index=True, unique=True)
        email = db.Column(db.String(120), index=True, unique=True)
        password_hash = db.Column(db.String(128))

        def __init__(self, username, email, password):
            self.username = username
            self.email = email
            self.password_hash = password

        def __str__(self):
            return 'User {}: {}'.format(self.username, self.email)

        def __repr__(self):
            return '<User {}>'.format(self.username)

    class UserDAO(object):
        def find_user_by_name(self, username):
            return User.query.filter_by(username=username).first()

        def find_user_by_id(self, id):
            return User.query.filter_by(id=id).first()

        def create_user(self, username, email, password):
            user = User(username, email, password)
            db.session.add(user)
            db.session.commit()
            return user

    return UserDAO()


def setup_apikey_db(db):
    class UserKeys(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64), index=True, unique=True)
        apikey = db.Column(db.String(64), unique=True)

        def __init__(self, username):
            self.username = username
            self.apikey = str(uuid.uuid1())

    class ApikeyDAO(object):
        def find_apikey_by_name(self, username):
            return UserKeys.query.filter_by(username=username).first()

        def create_apikey(self, username):
            apikey = UserKeys(username)
            db.session.add(apikey)
            db.session.commit()
            return apikey

    return ApikeyDAO()
