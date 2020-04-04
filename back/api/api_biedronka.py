from flask import Blueprint, current_app, request, jsonify

api_biedronka = Blueprint('api_biedronka', __name__)


@api_biedronka.record
def record(state):
    db = state.app.config.get("biedronka.db")
    if db is None:
        raise Exception("This blueprint expects you to provide "
                        "database access through biedronka.db")


@api_biedronka.route('/api/biedronka', methods=['POST'])
def find_biedronka():
    db = current_app.config["biedronka.db"]
    adres = request.json['adres']
    biedronka = db.find_biedronka_by_adres(adres)
    if biedronka is None:
        biedronka = db.create_biedronka(adres)
    print(biedronka)
    return jsonify(id=biedronka.id, adres=biedronka.adres)
