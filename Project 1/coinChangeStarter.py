# Return a list representing a coin system
# that contains coins from pennies up to
# one hunder dollar bills
# NOTE: All of your coins/bills
# should be of the data type float

# Completed by Abhiraj Chatterjee
def init_StdSystem():
    '''
    >>> init_StdSystem()
    [100.0, 50.0, 20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    '''
    l = [100.0, 50.0, 20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    return l


# Write a function that makes a
# list containing all of the standard
# coins up to the inputted max coin value.
# If max_val is none, return the standard system.

# Completed by Abhiraj Chatterjee
def init_CoinSystem(max_val):
    '''
    >>> init_CoinSystem(5)
    [5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    >>> init_CoinSystem(1)
    [1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    >>> init_CoinSystem(-1)
    'error'
    '''
    li = []
    li = init_StdSystem()
    if isinstance(max_val, int) and max_val in li:
      ind = li.index(max_val)
      return li[ind:]
    elif max_val == None:
      return li
    else:
      return 'error'


# Write a function that takes in a coin system
# and creates a dictionary that contains
# each coin as a key with each coin having
# an associated value of 0.

# Completed by Abhiraj Chatterjee
def init_ChangeDict(coin_system):
    '''
    >>> C = init_CoinSystem(1)
    >>> init_ChangeDict(C)
    {1.0: 0, 0.5: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    >>> S = init_StdSystem()
    >>> init_ChangeDict(S)
    {100.0: 0, 50.0: 0, 20.0: 0, 10.0: 0, 5.0: 0, 1.0: 0, 0.5: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    '''
    if isinstance(coin_system,list):
        dictionary = {}
        for item in coin_system:
            dictionary[item] = 0
        return dictionary
    else:
        return 'error'


# Check if it is possible to give
# exact change with the given coin system
# For simplicity's sake, you should just
# check that the money is at least greater than
# the smallest available coin.

# Completed by Abhiraj Chatterjee
def isValidChange(money, coin_system):
    '''
    >>> S = init_StdSystem()
    >>> isValidChange(.001, S)
    False
    >>> isValidChange(.15, S)
    True
    '''
    if money >= coin_system[len(coin_system)-1]:
        return True
    else:
        return False


# If coin change cannot be made, return an error message.
# Return a tuple in the form (min_coins, coin_dict)
# where min_coins is the minimum number of coins required
# and coin_dict is a dictionary that returns how many
# of each coin was used.

# Completed by Abhiraj Chatterjee
def coinChange(money, max_coin_val=None):
    '''
    >>> coinChange(1)
    (1, {100.0: 0, 50.0: 0, 20.0: 0, 10.0: 0, 5.0: 0, 1.0: 1, 0.5: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0})
    >>> coinChange(5.75)
    (3, {100.0: 0, 50.0: 0, 20.0: 0, 10.0: 0, 5.0: 1, 1.0: 0, 0.5: 1, 0.25: 1, 0.1: 0, 0.05: 0, 0.01: 0})
    '''
    denom = init_CoinSystem(max_coin_val)
    denom_count = init_ChangeDict(denom)
    c = 0
    k = 0
    if isValidChange(money, denom):
        while money != 0 and k < len(denom):
            if money < denom[k]:
                k += 1
            else:
                money -= denom[k]
                c += 1
                denom_count[denom[k]] += 1
        if money == 0:
            return (c, denom_count)
        else:
            return 'error'
    else:
        return 'error'
