def view(text, result):
    print("{} {}".format(text, result))


def input_data(text):
    return input(text)


def log_viev(filename):
    with open(filename, "r") as data:
        print(data.read())


# log_viev("log.csv")
