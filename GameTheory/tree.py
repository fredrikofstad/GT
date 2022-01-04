class TreeNode:
    def __init__(self, name, player = None, payoff = [None]):
        self.name = name
        self.children = []
        self.parent = None
        self.player = player
        self.strategy = ""
        self.payoff = payoff
        self.endnode = False if payoff[0] is None else True

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    # TODO: Make game class
    def calculate_payoff(self):
        if self.endnode == True:
            return self.payoff, self.name
        payoff, strategy = None, None
        for child in self.children:
            child_payoff, child_strategy = child.calculate_payoff()
            if payoff is None:
                payoff, strategy = child_payoff, child_strategy
            elif child_payoff[self.player] > payoff[self.player]:
                payoff, strategy = child_payoff, child_strategy
        return payoff, strategy


    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        space = ' ' * self.get_level() * 3
        if(self.endnode):
            print(space + self.name, self.payoff)
        else:
            print(space + self.name)
        if self.children:
            for child in self.children:
                 child.print_tree()

## Testing ##

def build_tree(): 
    root = TreeNode("Do action", 0)

    punish = TreeNode("punish", 1)
    accept = TreeNode("accept", None, [0,2])
    root.add_child(punish)
    root.add_child(accept)

    punish.add_child(TreeNode("retaliate", None, [3,4]))
    punish.add_child(TreeNode("nothing", None, [10,2]))

    root.print_tree()

    print(root.calculate_payoff())

    print("END")

if __name__ == '__main__':
    build_tree()