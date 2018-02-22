import Cards as cd

class Deck:
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(cd.Card(suit, rank))
    
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s
                
    def print_deck(self):
        for card in self.cards:
            print(card)
    
    
        


red_deck = Deck()
blue_deck = Deck()
print(blue_deck)

    
