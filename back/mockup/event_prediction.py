import random
from datetime import datetime, timedelta

from flask import Blueprint

predictions = Blueprint('predictions', __name__)

time_window = 3


@predictions.route('/api/mock/<timestamp>')
def mock_event_prediction(timestamp):
    req_timestamp = datetime.fromtimestamp(int(timestamp))
    print(req_timestamp)
    response = []
    for i in range(-time_window, time_window + 1):
        i_time = req_timestamp + timedelta(hours=i)
        i_time_str = i_time.time().__format__('%H:%M:%S')
        response.append((i_time_str, random.random()))

    return response.__str__()
