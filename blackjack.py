import random 

cards = []
for s in ['C','S', 'D', 'H']:
  for v in range(1,14):
    v = str(v)
    cards.append(s+v)


dealer_cards = random.choices(cards, k=2)

for x in dealer_cards:
  cards.remove(x)

player_cards = random.choices(cards, k=2)

for x in player_cards:
  cards.remove(x)

nv = 0

for v in player_cards:
  if int(v[1:]) < 11:
    nv += int(v[1:])
  elif int(v[1:]) < 13:
    nv += 10

print(nv)

print(player_cards)
print(dealer_cards)

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