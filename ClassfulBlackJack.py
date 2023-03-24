import os
import random
import time
import sys

class Player:
  def __init__(self):
    self.cards1 = []
    self.cards1value = 0
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
      try:
        self.presentdeck.remove(x)
      except ValueError:
        pass
    player.cards1 = random.choices(self.presentdeck, k=2)
    for x in player.cards1:
      try:
        self.presentdeck.remove(x) 
      except ValueError: 
        pass
    eval.evaluate('initial_distribution')
  def twist(self, x):
    if x == 'player':
      time.sleep(1)
      player.cards1.append(''.join(random.choices(self.presentdeck, k=1)))
      self.presentdeck.remove(player.cards1[-1])
      eval.evaluate('player')
    if x == 'dealer':
      time.sleep(1)
      dap.cards.append(''.join(random.choices(self.presentdeck, k=1)))
      self.presentdeck.remove(dap.cards[-1])
      eval.evaluate('dealer')

class Evaluator:
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
      eval.value_checker('initial_distribution')
    elif x == 'player' and len(player.cards1) > 2:
      player_twist = player.cards1[-1]
      player_twist = player_twist.split()
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
      eval.value_checker('player')
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
      return eval.dealer_value_checker()
  def value_checker(self, x):
    display.general_output()
    if player.cards1value == 21:
      print("The dealer will now attempt 21 in as many or less cards.")
      eval.dealer_value_checker()
    elif player.cards1value < 21:
      x = input('Value is less than 21, do you wish to stick (S) or twist (T)?')
      if x == 'S':
        eval.dealer_value_checker()
      if x == 'T':
        dad.twist('player')
    elif player.cards1value > 21:
      print("Bust! You lose.")
      bet.return_on_bet('Loss')
  def dealer_value_checker(self):
    display.general_output()
    if dap.cardsvalue < 17:
      dad.twist('dealer')
      eval.dealer_value_checker()
    elif dap.cardsvalue >= 17:
      eval.value_comparison()
  def value_comparison(self):
    if player.cards1value <=21 and dap.cardsvalue <= 21:
      if player.cards1value == dap.cardsvalue:
        print('Tie.')
        bet.return_on_bet('Tie')
      elif player.cards1value == 21 and dap.cardsvalue != 21:
        if len(player.cards1) == 2:
          print("Blackjack win!")
          bet.return_on_bet("Blackjack win")
        elif len(player.cards1) > 2:
          print("You win!")
          bet.return_on_bet('Win')
      elif player.cards1value != 21 and dap.cardsvalue == 21:
        if len(dap.cards) == 2:
          print("Dealer has Blackjack! You lose.")
          bet.return_on_bet('Loss')
        elif len(dap.cards) > 2:
          print("Dealer has 21, you lose!")
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
      elif int(21 - player.cards1value) > int(21 - dap.cardsvalue):
        print('You lose.')
        bet.return_on_bet('Loss')
    if dap.cardsvalue > 21:
      print("Dealer bust! You win.")
      if len(player.cards1) > 2:
        bet.return_on_bet('Win')
      elif len(player.cards1) == 2:
        bet.return_on_bet('Blackjack win')

class BetHandler:
  def placing_bet(self):
    os.system('clear')
    player.bet = 0
    player.cards1value = 0
    dap.cardsvalue = 0 
    x = input(f"\nYou have {player.purse}$. Place your bet: ")
    if float(x) > player.purse:
      print("Bet too large, insufficient funds.")
      return self.placing_bet()
    if x == 0:
      print("Bet must have a value greater than 0.")
      return self.placing_bet()
    elif float(x) < player.purse:
      player.bet = float(x)
      player.purse = player.purse - player.bet
    return dad.first_distribution()
  def return_on_bet(self, x):
    if x == 'Tie':
      player.purse = player.purse + player.bet
      print(f"\n{player.bet}$ was returned to your purse.")
      display.carry_on()
    if x == 'Win':
      n = player.bet*2
      player.purse = player.purse + n
      print(f"\nYou won {n}$, you now have {player.purse}$.")
      display.carry_on()
    if x == 'Loss':
      print(f"\nYou lost {player.bet}$, you now have {player.purse}$.")
      if player.purse <= 0:
        d = input("\nYou're broke! Restart (R) or quit (Q): ")
        if d == 'R':
          bet.placing_bet()
        if d == 'Q':
          print("Adieu.")
          sys.exit()
      display.carry_on()
    if x == 'Blackjack win':
      n = player.bet*2.5
      player.purse = player.purse + n
      print(f"\nYou won {n}$, you now have {player.purse}$.")
      display.carry_on()

class Display:
  def unicode_output(self, x): 
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
    if len(x) == len (output_hand):
      return output_hand
  def general_output(self):
    player_cards_unicode = ''.join(display.unicode_output(player.cards1))
    dealer_cards_unicode = ''.join(display.unicode_output(dap.cards))
    os.system('clear')
    print(f"""
Your hand is {player_cards_unicode}, valued at {player.cards1value}.\n
Dealer hand is {dealer_cards_unicode} valued at {dap.cardsvalue}.\n
Your bet is {player.bet}$ and your purse has {player.purse}$.\n
    """)
  def carry_on(self):
    x = input("\nLet's play another round? Y/N: ")
    if x == 'N':
      os.system('exit')
    if x == 'Y':
      bet.placing_bet()


dad = DealerAsDealer()
player = Player()
dap = DealerAsPlayer()
eval = Evaluator()
display = Display()
bet = BetHandler()

bet.placing_bet()