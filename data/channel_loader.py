CHANNEL_FILE = "data/channels.txt"

def get_X_values():
    X_values = []
    X_text = []
    file = None

    try:
        with open(CHANNEL_FILE, "r") as file:
            read_file = file.read()
    finally:
        if file is not None:
            file.close()

    if read_file:
        X_text = read_file.split(", ")
        X_text.remove("X")

    try:
        for value in X_text:
            X_values.append(float(value))
    except ValueError as e:
        print("Invalid x value found {}".format(value))

    return X_values