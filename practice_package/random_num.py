import random

print("For the rand_num function, the argument is the length of the random number")
def rand_num(numlen=7):
    return int("".join([str(random.randint(0,9)) for _ in range(numlen)]))