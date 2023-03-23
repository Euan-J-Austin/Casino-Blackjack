#when player twists and no bust, bet resets to 0 ... fix this!

import os
import random
import time
import sys


class Player:

  def __init__(self):
    self.cards1 = []
    self.cards2 = []  #in the case of Split
    self.cards1value = 0
    self.cards2value = 0
    self.purse = 100.0
    self.bet = 0.0


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
    if x == 'initial_distribution':
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
      player_twist = player_twist.split() #use list here?
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
      return eval.dealervaluechecker()

  def valuechecker(self, x):
    display.general_output()
    if player.cards1value == 21:
      print("The dealer will now attempt 21 in as many or less cards.")
      time.sleep(3)
      eval.dealervaluechecker()
    elif player.cards1value < 21:
      x = input('Value is less than 21, do you wish to stick or twist?')
      if x == 'S':
        eval.dealervaluechecker()
      if x == 'T':
        dad.twist('player')
    elif player.cards1value > 21:
      print("Bust! You lose.")
      bet.return_on_bet('Loss')

  def dealervaluechecker(self):
    display.general_output()
    if dap.cardsvalue < 17:
      dad.twist('dealer')
      eval.dealervaluechecker()
    elif dap.cardsvalue >= 17:
      eval.valuecomparison()

  def valuecomparison(self):
    #next, sort bets and unicode output
    if player.cards1value <=21 and dap.cardsvalue <= 21:
      if player.cards1value == dap.cardsvalue:
        print('Tie.')
        bet.return_on_bet('Tie')
      elif player.cards1value == 21 and dap.cardsvalue != 21:
        print("Blackjack win!")
        bet.return_on_bet("Blackjack win")
      elif player.cards1value != 21 and dap.cardsvalue == 21: 
        print("Dealer has Blackjack! You lose.")
        bet.return_on_bet('Loss')
      elif player.cards1value == 21 and dap.cardsvalue == 21:
        if len(player.cards1) < len (dap.cards):
          print("You win! 21 in less cards than dealer.")
          bet.return_on_bet('Win')
        elif len(player.cards1) > len (dap.cards):
          print("You lose! Dealer has 21 in less cards.")
          bet.return_on_bet('Loss')
        elif len(player.cards1) == len (dap.cards):
          if len(player.cards1) == 2 and len (dap.cards) == 2:
            print("Tie! Both you and dealer achieved blackjack!")
            bet.return_on_bet('Tie')
          else:
            print("Tie! Both achieved 21 in same amount of cards.")
            bet.return_on_bet('Tie')
      elif int(21 - player.cards1value) < int(21 - dap.cardsvalue):
        print('You win.')
        bet.return_on_bet('Win')
        #print victory, distribute bets accordingly
      elif int(21 - player.cards1value) > int(21 - dap.cardsvalue):
        print('You lose.')
        bet.return_on_bet('Loss')
        #print lost, distribute bets
    if dap.cardsvalue > 21: #already accounted for player cards's value > 21
      print("Dealer bust! You win.")
      bet.return_on_bet('Win')


class BetHandler:
  def __init__(self):
    pass
  def placingbet(self):
    player.bet = 0 #reset to 0 following previous round
    player.cards1value = 0 # create a separate class/method for reseting?
    dap.cardsvalue = 0 
    x = input('Place your bet: ')
    if float(x) > player.purse:
      print("Bet too large, insufficient funds.")
      return self.placingbet()
    if x == 0:
      print("Bet must have a value greater than 0.")
      return self.placingbet()
    elif float(x) < player.purse:
      player.bet = float(x)
      player.purse = player.purse - player.bet
    return dad.first_distribution()
  def return_on_bet(self, x):
    #reset bet to 0? 
    if x == 'Tie':
      player.purse = player.purse + player.bet
      print(f"{player.bet}$ was returned to your purse.")
      bet.placingbet()
    if x == 'Win':
      n = player.bet*2
      player.purse = player.purse + n
      print(f"You won {n}$, you now have {player.purse}$.")
      bet.placingbet()
    if x == 'Loss':
      print(f"You lost {player.bet}$, you now have {player.purse}$.")
      if player.purse <= 0:
        d = input("You're broke! GAME OVER. Type R to Restart or Q to quit: ")
        if d == 'R':
          bet.placingbet()
        if d == 'Q':
          print("Adieu.")
          sys.exit()
      bet.placingbet()
    if x == 'Blackjack win':
      n = player.bet*2.5
      player.purse = player.purse + n
      print(f"You won {n}, you now have {player.purse}$.")
      bet.placingbet()

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