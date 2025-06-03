class History:
    def __init__(self, Dealer, Player, Match, PlayerName):
        self.Dealer = Dealer
        self.Player = Player
        self.Match = Match
        self.PlayerName = PlayerName

    def __str__(self):
        return f" █ Dealer: {self.Dealer} █ {self.PlayerName}: {self.Player} █ {self.Match}"