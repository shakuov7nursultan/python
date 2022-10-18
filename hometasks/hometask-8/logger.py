from datetime import datetime as dt

# import json_creator as jcr


def logger(text, data):
    time = dt.now().strftime("%H:%M:%S")
    log_string = f"{time}; {text}; {data}\n"
    # jcr.create_log_json(log_string)
    with open("log.csv", "a") as file:
        file.write(log_string)
