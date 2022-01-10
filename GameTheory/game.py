import tree

class Game:
    def __init__(self):
        pass
    def add_node():
        pass

def build_tree(): 
    root = Node("Do action", 0)

    punish = Node("punish", 1)
    accept = Node("accept", None, [5,2])
    root.add_child(punish)
    root.add_child(accept)

    punish.add_child(Node("retaliate", None, [3,4]))
    punish.add_child(Node("nothing", None, [10,2]))

    root.print_tree()

    print(root.calculate_payoff())

    print("END")

if __name__ == '__main__':
    build_tree()



