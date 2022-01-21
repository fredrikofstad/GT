from tree import Node

# Extensive sequential form game
class Game:
    def __init__(self):
        self.root = Node("Root", 0)
    def calculate_payoff(self):
        self.root.calculate_payoff()


def build_tree(): 
    game = Game()
    # create nodes:
    action1 = Node("Do action", 1)
    # add nodes as child
    game.root.add_child(action1)
    game.root.add_child(Node("Nothing", None, [2,5]))

    action1.add_child(Node("punish", None, [1,2]))
    action1.add_child(Node("accept", None, [10,1]))

    game.root.print_tree()
    print("::")
    print(game.root.calculate_payoff())


if __name__ == '__main__':
    build_tree()



