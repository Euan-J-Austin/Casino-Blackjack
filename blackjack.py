import random 

cards = []
for s in ['C', 'S', 'D', 'H']:
  for v in range(1,14):
    v = str(v)
    cards.append(s+v)


dealer_cards = random.choices(cards, k=2)

for x in dealer_cards:
  cards.remove(x)

player_cards = random.choices(cards, k=2)

for x in player_cards:
  cards.remove(x)

players_value = 0
dealers_value = 0

#Ace will have a value of 11 unless player exceeds 21, then equal to 1 

# 1 = Ace
# 11 = J
# 12 = Q
# 13 = K

for v in player_cards:
  if 1 < int(v[1:]) < 11:
    players_value += int(v[1:])
  elif 10 < int(v[1:]) <= 13:
    players_value += 10
  elif int(v[1:]) == 1:
    if players_value <= 21:
      players_value += 11
    elif players_value > 21:
      players_value += 1

for v in dealer_cards:
  if 1 < int(v[1:]) < 11:
    dealers_value += int(v[1:])
  elif 10 < int(v[1:]) <= 13:
    dealers_value += 10
  elif int(v[1:]) == 1:
    if dealers_value <= 21:
      dealers_value += 11
    elif dealers_value > 21:
      dealers_value += 1

print(players_value)
print(dealers_value)

print(player_cards)
print(dealer_cards)

def output(x):
  output_hand = []
  for s in x:
    #CLUBS
    if s == 'C1':
      output_hand.append('\u2663A')
    elif s == 'C11':
      output_hand.append('\u2663J')
    elif s == 'C12':
      output_hand.append('\u2663Q')
    elif s == 'C13':
      output_hand.append('\u2663K')
    elif s[0] == 'C':
      output_hand.append(f'\u2663{s[1:]}')
    #SPADES
    if s == 'S1':
      output_hand.append('\u2660A')
    elif s == 'S11':
      output_hand.append('\u2660J')
    elif s == 'S12':
      output_hand.append('\u2660Q')
    elif s == 'S13':
      output_hand.append('\u2660K')
    elif s[0] == 'S':
      output_hand.append(f'\u2660{s[1:]}')
    #DIAMONDS
    if s == 'D1':
      output_hand.append('\u2666A')
    elif s == 'D11':
      output_hand.append('\u2666J')
    elif s == 'D12':
      output_hand.append('\u2666Q')
    elif s == 'D13':
      output_hand.append('\u2666K')
    elif s[0] == 'D':
      output_hand.append(f'\u2666{s[1:]}')
    #HEARTS
    if s == 'H1':
      output_hand.append('\u2665A')
    elif s == 'H11':
      output_hand.append('\u2665J')
    elif s == 'H12':
      output_hand.append('\u2665Q')
    elif s == 'H13':
      output_hand.append('\u2665K')
    elif s[0] == 'H':
      output_hand.append(f'\u2665{s[1:]}')
  if x == player_cards:
    return print(f"Your hand is: {''.join(output_hand)}, valued at {players_value}")
  else:
    return print(f"Dealer hand is: {''.join(output_hand)}, valued at {dealers_value}.")

output(player_cards)
output(dealer_cards)


      
    
#evaluator

# def dealer_cards_value(x):
  

  
# def player_cards_value(x):
#   card_one, card_two = x[0], x[1]
#   if card_one[1] > 10:
#       card_one = [card_one[0], 10]
#   if card_two[1] > 10:
#       card_two = [card_two[0], 10]
#   print(card_one[1]+card_two[1])
    
    
      
# dealer_cards_value(dealer_cards)
# player_cards_value(player_cards)