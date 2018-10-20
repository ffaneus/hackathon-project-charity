class Donors():
    def __init__(self, item, amount, name):
        self.item = item
        self.amount = amount
        self.name = name
    def donate(self):
        """Donate the item(s)/ send to NPO"""
        donors.append(self)