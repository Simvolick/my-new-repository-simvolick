import random

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")

    def getValue(self):
        return int(self.value)

    def assignValue(self):
        cardScore = int
        if int(self.value) == 1:
            score = 11
            return score
        if int(self.value) == 11 == 12 == 13:
            score = 10
            return score
        if int(self.value) == (2, 11):
            score = self.value
            return score
        else:
            score = self.value
            return score




class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player:

    def __init__(self, name):

        self.name = name
        self.hand = []
        self.score = 0

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def showFirstCardDealer(self):
        for card in self.hand:
            card.show()
            break

    def getScore(self):
        self.score = 0
        for v in self.hand:
            self.score += v.assignValue()

    def scoreNow(self):
        #print(f"The score now is {self.score}")
        return self.score

    def handScore(self):
        for v in self.hand:
            self.score += v.getValue()


    def handScoreNow(self):
        print(f"The score now is {self.score}")
        return self.score






class Account:

#Need to add while loops to check for bet balance and also for inputing bet amount being an int
    def __init__(self, balance = 0):
        self.balance = balance

    def topup(self, deposit):
        self.deposit = deposit
        self.balance += deposit

    def bet(self, amount=0):

        self.amount = amount

        if amount > self.balance:
            print(f"Not enough money for bet of {amount}! Lower your bet or top up.")
        else:
            print(f"Bet of {amount} has been registered")
            self.balance -= amount

    def displayBalance(self):
        return print(f"Your balance now is: {self.balance}")

    def betTie(self):
        self.balance += self.amount

    def betWon(self):
        self.balance += (self.amount * 2)

if __name__ == "__main__":
    startingMoney = Account(500)
    startingMoney.bet(50)
    startingMoney.displayBalance()
    startingMoney.bet(500)


    deck = Deck()
    deck.shuffle()

    bob = Player('Bob')
    bob.draw(deck)
    bob.showHand()

'''
card = deck.drawCard()

card.show()
'''