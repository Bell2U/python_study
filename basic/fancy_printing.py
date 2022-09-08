import random, time, string

""" 
An example from Skynet project part 1 and 2:
"""
def generate_random_string(alphabet=None, length=8, exact=False):
    if not alphabet:
        alphabet = string.ascii_letters + string.digits
    """
    The line below is called a list comprehension and is the same as:
    letters = []
    for i in range(length):
        # Select a random letter from the alphabet and add it to letters
        letters.append(random.choice(alphabet))
    # Join the letters together with no separator
    return ''.join(letters)
    """
    if not exact:
        length = random.randint(length-4 if length-4 > 0 else 1,length+4)
    return ''.join(random.choice(alphabet) for x in range(length))

def bitcoin_mine():
    frames = "\\|/-"
    for i in range(8):
        print("\r%c" % frames[i % len(frames)], end="")
        time.sleep(0.1)
    print()
    # Bitcoin addresses start with a 3 or 1
    return random.choice("13") + generate_random_string(length=30)
# print(bitcoin_mine())

def test1():
    # https://stackoverflow.com/questions/18692617/how-does-r-carriage-return-work-in-python/18692647
    print('\r123abc', end='')
    print('\r456')
    print('\r789')
# test1()

def test2():
    i = 1
    while i <= 10:
        print(f'\r{i}/10', end='')
        time.sleep(0.2)
        i += 1
    print()
# test2()
