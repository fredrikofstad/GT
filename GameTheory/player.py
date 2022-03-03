class Player:
    counter = 0

    def __init__(self, name=None, order=None, prefs=None):
        self._name = name if name is not None else f"Player {Player.count()}"
        self._order = order if order is not None else Player.count()
        self._prefs = prefs
        Player.increment()

    def __str__(self):
        return f"{self._name} : Player {self._order} Preference: {self._prefs} |"

    def set_prefs(self, prefs):
        self._prefs = prefs


    @staticmethod
    def increment():
        Player.counter += 1

    @staticmethod
    def count():
        return Player.counter


player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player(name="USA")

player2.set_prefs({"outcome1": 2, "Outcome3": 4, "Outcome2": 1})

print(player1, player2, player3, player4)
