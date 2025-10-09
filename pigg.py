coins = 100
coins = 100 + 500

print(" I have:", coins, "coins")


coins = -999


class piggybank:
    def __init__(self, coins):
        self.coins = coins
joela = piggybank(200,000)
print("joela's box has: ", joela.coins,"q")

class piggybank:
    def __init__(self, coins):
        self._coins = coins
        self.put_in(coins)
def put_in(self, coins):


#setter
    def put_in(self, amount):
        if amount <= 0:
            raise ValueError("add real money")
        self._coins += amount
#getter
    def take_out(self,amount):
        if amount <= 0:
            raise ValueError(" Be real.")
        if amount > self.coins:
            raise ValueError("money is coming")
        self.coins -= amount


        def how_much(self, coins):
            return self._coins 


joela = piggybank(200,000)
print("joela's box has: ", joela.coins,"q")

