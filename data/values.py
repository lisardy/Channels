PARAMETERS_FILE = "data/parameters.txt"


class Values():
    m_value = None
    c_value = None

    def __init__(self):
        self._load_parameters()

    def _load_parameters(self):
        file = None

        try:
            with open(PARAMETERS_FILE, "r") as file:
                pass
                for line in file:
                    split_values = line.split(", ")

                    if len(split_values) > 1:
                        if split_values[0] == "m":
                            self.m_value = float(split_values[1])

                        if split_values[0] == "c":
                            self.c_value = float(split_values[1])
        finally:
            if file:
                file.close()

    def get_m(self):
        return self.m_value

    def get_c(self):
        return self.c_value