from datetime import datetime

def unixtime_date(input):
    timestamp = input
    dt_object = datetime.fromtimestamp(timestamp)
    rdt_string = dt_object.strftime("%Y-%m-%d %H:%M:%S")
    return rdt_string