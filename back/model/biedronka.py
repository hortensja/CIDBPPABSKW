def setup_biedronka_db(db):
    class Biedronka(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        adres = db.Column(db.String(256), unique=True)

        def __init__(self, adres):
            self.adres = adres

        def __str__(self):
            return '<Biedrusko {}: {}>'.format(self.id, self.adres)

    class BiedronkaDAO(object):
        def find_biedronka_by_adres(self, adres):
            return Biedronka.query.filter_by(adres=adres).first()

        def create_biedronka(self, adres):
            biedronka = Biedronka(adres)
            db.session.add(biedronka)
            db.session.commit()
            return biedronka

    return BiedronkaDAO()
