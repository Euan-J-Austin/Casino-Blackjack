cards = []
for s in ['\u2660', '\u2663', '\u2662', '\u2661']:
  for v in range(1,14):
    cards.append([s, v])

for x in cards:
  if x[1] == 1:
    x[1] == 'A'

print(cards)