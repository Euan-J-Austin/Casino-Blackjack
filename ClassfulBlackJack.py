#loop dealer twist until >= 17
import os
import random


class Player:

  def __init__(self):
    self.cards1 = []
    self.cards2 = []  #in the case of Split
    self.cards1value = 0
    self.cards2value = 0
    self.purse = 100
    self.bet = 0


class DealerAsPlayer:

  def __init__(self):
    self.cards = []
    self.cardsvalue = 0
    self.bank = []


class DealerAsDealer:

  def __init__(self):
    self.presentdeck = [
      str(v) + s for v in range(1, 14) for s in ['C', 'S', 'D', 'H']
    ]

  def first_distribution(self):
    dap.cards = random.choices(self.presentdeck, k=1)
    for x in dap.cards:
      self.presentdeck.remove(x)
    player.cards1 = random.choices(self.presentdeck, k=2)
    for x in player.cards1:
      self.presentdeck.remove(x)
    eval.evaluate('initial_distribution')

  def twist(self, x):
    if x == 'player':
      player.cards1.append(''.join(random.choices(self.presentdeck, k=1)))
      self.presentdeck.remove(player.cards1[-1])
      eval.evaluate('player')
    if x == 'dealer':
      dap.cards.append(''.join(random.choices(self.presentdeck, k=1)))
      self.presentdeck.remove(dap.cards[-1])
      eval.evaluate('dealer')


class Evaluator:

  def __init__(self):
    pass

  def evaluate(self, x):
    if x == 'initial_distribution' and len(player.cards1) <= 2 and len(
        dap.cards) == 1:
      for v in player.cards1:
        if 1 < int(v[:-1]) < 11:
          player.cards1value += int(v[:-1])
        elif 10 < int(v[:-1]) <= 13:
          player.cards1value += 10
        elif int(v[:-1]) == 1:
          if player.cards1value + 11 <= 21:
            player.cards1value += 11
          elif player.cards1value > 21:
            player.cards1value += 1
      for v in dap.cards:
        if 1 < int(v[:-1]) < 11:
          dap.cardsvalue += int(v[:-1])
        elif 10 < int(v[:-1]) <= 13:
          dap.cardsvalue += 10
        elif int(v[:-1]) == 1:
          if dap.cardsvalue + 11 <= 21:
            dap.cardsvalue += 11
          elif dap.cardsvalue > 21:
            dap.cardsvalue += 1
      eval.valuechecker('initial_distribution')
    elif x == 'player' and len(player.cards1) > 2:  #FOR PLAYER TWIST
      player_twist = player.cards1[-1]
      player_twist = list(player_twist.split())
      for v in player_twist:
        if 1 < int(v[:-1]) < 11:
          player.cards1value += int(v[:-1])
        elif 10 < int(v[:-1]) <= 13:
          player.cards1value += 10
        elif int(v[:-1]) == 1:
          if player.cards1value + 11 <= 21:
            player.cards1value += 11
          elif player.cards1value > 21:
            player.cards1value += 1
      eval.valuechecker('player')
    elif x == 'dealer' and len(dap.cards) > 1:
      dealer_twist = dap.cards[-1]
      dealer_twist = list(dealer_twist.split())
      for v in dealer_twist:
        if 1 < int(v[:-1]) < 11:
          dap.cardsvalue += int(v[:-1])
        elif 10 < int(v[:-1]) <= 13:
          dap.cardsvalue += 10
        elif int(v[:-1]) == 1:
          if dap.cardsvalue + 11 <= 21:
            dap.cardsvalue += 11
          elif dap.cardsvalue > 21:
            dap.cardsvalue += 1
      return eval.valuechecker('dealer')

  def valuechecker(self, x):
    display.general_output()
    if player.cards1value == 21 and x == 'initial_distribution' or x == 'player':
      print('Blackjack, you win!')  #not true, dealer must not have 21
    elif player.cards1value > 21 and x == 'initial_distribution' or x == 'player':
      print('Bust!')
    elif player.cards1value < 21 and x == 'initial_distribution' or x == 'player':
      x = input('Value is less than 21, do you wish to stick or twist?')
      if x == 'S':
        eval.dealervaluechecker()
      if x == 'T':
        dad.twist('player')

  def dealervaluechecker(self):
    #does recieve up to date value a
    if dap.cardsvalue < 17:
      dad.twist('dealer')
      #Recursion
      eval.dealervaluechecker()
    elif dap.cardsvalue >= 17:
      eval.valuecomparison()

  def valuecomparison(self):
    #next, sort bets and unicode output
    if player.cards1value == dap.cardsvalue:
      print('Tie')
      #print tie, distribute bets accordingly
    elif player.cards1value > dap.cardsvalue:
      print('Win')
      #print victory, distribute bets accordingly
    elif player.cards1value < dap.cardsvalue:
      print('Loss')
      #print lost, distribute bets


class BetHandler:

  def __init__(self):
    pass

  def placingbet(self):
    print(player.purse)
    print(player.bet)
    x = input('Place your bet: ')
    if int(x) > player.purse:
      print("Bet too large, insufficient funds.")
      return self.placingbet()
    if int(x) < player.purse:
      player.bet = int(x)
      player.purse = player.purse - player.bet
    return dad.first_distribution()


class PlayerDecisions:

  def __init__(self):
    pass


class Display:

  def __init__(self):
    pass

  def unicode_output(
      self, x):  #change to unicode formatting function, new standard output
    output_hand = []
    for s in x:
      #CLUBS
      if s == '1C':
        output_hand.append('A\u2663')
      elif s == '11C':
        output_hand.append('J\u2663')
      elif s == '12C':
        output_hand.append('Q\u2663')
      elif s == '13C':
        output_hand.append('K\u2663')
      elif s[-1] == 'C':
        output_hand.append(f'{s[:-1]}\u2663')
      #SPADES
      if s == '1S':
        output_hand.append('A\u2660')
      elif s == '11S':
        output_hand.append('J\u2660')
      elif s == '12S':
        output_hand.append('Q\u2660')
      elif s == '13S':
        output_hand.append('K\u2660')
      elif s[-1] == 'S':
        output_hand.append(f'{s[:-1]}\u2660')
      #DIAMONDS
      if s == '1D':
        output_hand.append('A\u2666')
      elif s == '11D':
        output_hand.append('J\u2666')
      elif s == '12D':
        output_hand.append('Q\u2666')
      elif s == '13D':
        output_hand.append('K\u2666')
      elif s[-1] == 'D':
        output_hand.append(f'{s[:-1]}\u2666')
      #HEARTS
      if s == '1H':
        output_hand.append('A\u2665')
      elif s == '11H':
        output_hand.append('J\u2665')
      elif s == '12H':
        output_hand.append('Q\u2665')
      elif s == '13H':
        output_hand.append('K\u2665')
      elif s[-1] == 'H':
        output_hand.append(f'{s[:-1]}\u2665')
    # if x == player.cards1:
    #   return print(
    #     f"Your hand is: {''.join(output_hand)}, valued at {player.cards1value}"
    #   )
    #   # if players_value > 21:
    #   #   print("YOUR BUST!")
    # else:
    #   return print(
    #     f"Dealer hand is: {''.join(output_hand)}, valued at {dap.cardsvalue}.")

    # #your cards and their value, dealer cards and their value, your bet, your purse
  def general_output(self):
    os.system('clear')
    print(f"""
    Your hand is {player.cards1}, valued at {player.cards1value}.
    Dealer hand is {dap.cards} valued at {dap.cardsvalue}.
    Your bet is {player.bet}$ and your purse has {player.purse}$.
    """)


dad = DealerAsDealer()
player = Player()
dap = DealerAsPlayer()
eval = Evaluator()
display = Display()
bet = BetHandler()
# dad.first_distribution()
bet.placingbet()

#
