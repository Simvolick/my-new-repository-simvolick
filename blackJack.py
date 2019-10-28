import main


print("Welcome to BlackJack")
replay = False
game_on = True
starting_money = main.Account(1000)
deck = main.Deck()
deck.shuffle()
bob = main.Player("Bob")
dealer = main.Player("Dealer")
bet = False
#card = main.Card(bob.hand)


while game_on == True or replay == True:
    bet = False
    if replay == True:
        deck = main.Deck()
        deck.shuffle()
        bob.hand = []
        dealer.hand = []
    while bet == False:
        global amount
        amount = input("Please state your bet: ")
        try:
            starting_money.bet(int(amount))
            starting_money.displayBalance()
            if int(amount) <= starting_money.balance:
                bet = True
        except:
            print('This is not an integer')


    dealer.draw(deck)
    bob.draw(deck)
    dealer.draw(deck)
    bob.draw(deck)
    dealer.showFirstCardDealer(), print('For Dealer')
    bob.showHand(), print('For Bob')
    bob.getScore()
    dealer.getScore()
    print('Players turn')
    print(f"Bobs score now is {bob.scoreNow()}")
    while bob.scoreNow() < 21:
        hit = input("Player do you wish to take another card? (y or n)")
        if hit[0].lower() == 'y':
            bob.draw(deck)
            bob.showHand()
            bob.getScore(), print('For Bob')
            print(f"Bobs score now is {bob.scoreNow()}")

        else:
            break
    print('Dealers turn')
    print(f"Dealers score now is {dealer.scoreNow()}")
    while dealer.scoreNow() < 17 and bob.scoreNow() < 21 and dealer.scoreNow() <= bob.scoreNow():
        dealer.showHand()
        print('\n')
        dealer.draw(deck)
        dealer.showHand()
        print('\n')
        dealer.getScore(), print('For Dealer')
        print(f"Dealers score now is {dealer.scoreNow()}")
        print('xd')
    if (bob.scoreNow() > dealer.scoreNow() and bob.scoreNow() <= 21) or \
            dealer.scoreNow() > 21:
        print('Player Wins!')
        starting_money.betWon()
        starting_money.displayBalance()
    elif bob.scoreNow() == dealer.scoreNow():
        starting_money.betTie()
        starting_money.displayBalance()
        print("It's a Tie!")
    else:
        print('Dealer Wins!')
    replay = input("Player do you wish play again? (y or n)")
    if replay[0].lower() == 'y':
        replay = True
    else:
        print('Thanks for playing!')
        game_on = False
