PARAMETERS_FILE = "parameters.txt"
CHANNELS_FILE = "channels.txt"


class Values():
    X_values = None
    m_value = None
    c_value = None

    def __init__(self):
        _load_values()

    def _load_values(self):
        pass

    def _load_parameters(self):
        pass

    def _load_channels(self):
        pass

    def get_X_values(self):
        return self.X_values

    def get_m(self):
        return self.m_value

    def get_c(self):
        return self.c_value