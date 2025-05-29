class History:
    def __init__(self, Dealer, Player, Match):
        self.Dealer = Dealer
        self.Player = Player
        self.Match = Match

    def __str__(self):
        return f" | Dealer: {self.Dealer} | Player: {self.Player} | {self.Match}"