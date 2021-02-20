'''Lucille spent 12% of her weekly earnings on
DVDs and deposited the rest into her savings
account. If she spent $42 on DVDs, how much
did she deposit into her savings Account?
'''
def calculateSavings(x, y):
  return (x * 100) / y - x

spendDVD = 42
spentRatio = 12
savings = calculateSavings(spendDVD, spentRatio)
print("The savings in her savings account is: ${:.2f}".format(savings))
