import datetime


def datetimeconverter(self):
    time_input = datetime.datetime.fromtimestamp(int(self))
    formatted_time = time_input.strftime('%H:%M')
    return formatted_time
