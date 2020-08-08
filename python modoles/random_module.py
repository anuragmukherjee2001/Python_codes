import random

# print(dir(random))              #shows all the methods present in the random module


# a = random.random()              #  craeting a random value (the type will be always float anad the range is (0.0 to 1.0))
# print(a)

# b = random.uniform(10,20)           #genarating a random variable within the given range
# print(b)

# c = random.randint(10,20)               #creates a random integer value within the given range
# print(c)

# d = random.randrange(1,10,2)            #parameters --> first - start value, second - end value, third - step value
# print(d)                                    #only 1,3,5,7,9 can apperar (displaying odd number in the given range)

# lst = ['win', 'lose', 'draw']

# e = random.choice(lst)                    # gives a value from the list
# print(e)

# colour = ['red', 'black', 'pink', 'blue']

# f = random.choices(colour,k = 6)            #creates a list of random items (k is the key value)
# print(f)

# deck = list(range(1,53))

# print(deck)

# g = random.shuffle(deck)                    #shuffled the numbers in the list
# print(deck)                                 #printing the shuffled list

# h = random.sample(deck,k = 10)                  #printing a sample of 10 random integers from a big list 
# print(h)

# i = random.getrandbits(3)                       # creating random integer in bit level
# print(i)