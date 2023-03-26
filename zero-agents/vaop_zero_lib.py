class Val:
    def __init__(self, val):
        self.val = val

    def is_usual(self):
        pass

    def is_selfref(self):
        pass

    def is_templ(self):
        pass

    def is_id(self):
        pass


class Card:
    def __init__(self, name, vals):
        self.name = name
        self.vals = vals


class Parser:
    def __init__(self):
        pass
        self.cards = []

    def add_card(self, name, vals):
        vals = [Val(val) for val in vals]
        self.cards.append(Card(name, vals))
        print(type(vals[0]))