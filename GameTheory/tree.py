class Node:
    def __init__(self, name, player=None, payoff=[None]):
        self.name = name
        self.children = []
        self.parent = None
        self.player = player
        self.payoff = payoff
        self.endnode = False if payoff[0] is None else True

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def calculate_payoff(self):
        if self.endnode:
            return self.payoff, self.name, [[0], [0]]
        payoff, strategy, pne= None, None, None
        for child in self.children:
            child_payoff, child_strategy, child_pne = child.calculate_payoff()
            if payoff is None:
                payoff, strategy, pne = child_payoff, child_strategy, child_pne
            elif child_payoff[self.player] > payoff[self.player]:
                payoff, strategy, pne = child_payoff, child_strategy, pne[self.player].append(child_strategy)
        return payoff, strategy, pne

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