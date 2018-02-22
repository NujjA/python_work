class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ['none', 'Ace', '2', '3', '4', '5', '6', '7', '8',
    '9', '10', 'Jack', 'Queen', 'King'] #aces low
    
    def __init__ (self, suit = 0, rank = 0):
        self.suit = suit
        self.rank = rank
        
    def __str__ (self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    #equals
    def __eq__(self, other):
        return self.cmp(other) == 0
        
    #less than or equal
    def __le__(self, other):
        return self.cmp(other) <= 0

    #greater than or equal
    def __ge__(self, other):
        return self.cmp(other) >= 0

    #greater than
    def __gt__(self, other):
        return self.cmp(other) > 0

    #less than
    def __lt__(self, other):
        return self.cmp(other) < 0

    #not equal
    def __ne__(self, other):
        return self.cmp(other) != 0
        
    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Suits are the same... check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # Ranks are the same... it's a tie
        return 0
        
        

card1 = Card(1, 11)
print(card1)
