class Pref:
    def __init__(self, value: int, name: str = None):
        self._value = value
        self._name = name if name is not None else str(value)

    def value(self):
        return self._value

    def name(self):
        return self._name

