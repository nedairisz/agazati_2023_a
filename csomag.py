class Csomag:
    def __init__(self, szelesseg:int, magassag:int, melyseg:int, suly:int):
        self.szelesseg=szelesseg
        self.magassag=magassag
        self.melyseg=melyseg
        self.suly=suly

    def __str__(self):
        return f"{self.szelesseg}x{self.magassag}x{self.melyseg}, súlya: {self.suly}kg."