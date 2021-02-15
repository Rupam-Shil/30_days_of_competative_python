'''Mr Richard Tupper is purchasing gifts for his
family. So far he has purchased the following:
1. 3 Sweaters, each valued at $68
2. One Computer game valued at $75
3. 2 bracelets each valued at $43
Later, he returned one of the bracelets for a full
refund and received a $10 rebate on the
Computer game. What is the total cost for the gifts
after the refund and rebate?
Calculation part of the program should be under three lines.'''

total_price_of_sweater = 68
no_of_sweaters = 3
total_price_of_computer_game = 75
no_of_computer_game = 1
total_price_of_bracelet = 43
no_of_bracelets = 2

return_bracelet_count = 1
rebate_on_computer_game = 10

total_gift_price = ((total_price_of_sweater * no_of_sweaters) + (total_price_of_computer_game * no_of_computer_game) + (total_price_of_bracelet* no_of_bracelets)) - ((total_price_of_bracelet * return_bracelet_count) +rebate_on_computer_game)
print(total_gift_price)
