import random

def ex1():

    r = range(10)
    it = iter(r)
    while True:
        try:
            if next(it) % 2 == 1:
                print(next(it))
        except StopIteration:
            break

def choose_randomly_from(data, count=1):

    i = 0
    while i < count:
        if i >= 1000:
            raise StopIteration()
        index = random.randint(0, len(data)-1)
        yield data[index]
        i += 1

def ex2():
    
    for c in choose_randomly_from('golf', 20):
        print(c)

if __name__ == "__main__":
    ex2()
