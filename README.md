A simple Blackjack simulator.

My third Python project!

The third of four 'simple' projects for my Python portfolio.

Following the advice of Andy Sterkowitz, my simple project would use the basic Python library; use less than 200 lines of code; use the CLI as opposed to GUI or WebApp.

What does it do?

I created a simple Blackjack simulator for a single player and a dealer. Simple meaning that although I used the casino rules as a loose guide, special plays like splitting or taking out insurance against a dealer Blackjack hand were not included because I ran over the 200 lines of code I had specified for a simple project (I allowed myself some margin for error as some of this was superfluous translation of the cards from a list format to a visually more pleasing unicode). It used some modules form the Python standard library such as time, system etc. I used the time module to make the dealing of cards feel more natural by sleeping the twist function and the dealer's play after the player decides to stick.

What doesn't it do?

By definition, the scope of a simple project is limited. There is no unit-testing so the rules specified in the input instruction have to be adhered to as exceptions can't be handled. Aforementioned, there are no special plays or bets. Lastly, the game is for one player and a dealer. I would like to return to the project at some point to re-make the conditional logic operations which I believe could be handled more elegantly. 

What went wrong the first time?

I made two attempts at this project. The first (fortunately short-lived)  envisioned the project as a text-based game, set in a casino, where Blackjack would feeature as one of the games that could be played. I struggled because I was not sure how all the functions and variables would relate to each other in a large project. On my second attempt, I focused only on creating a Blackjack game and after reading through the casino rules created a flow-chart. Having this flow-chart was a great help in envisioning what the classes should be and the conditional logis of evaluating the player's cards and bets.  
