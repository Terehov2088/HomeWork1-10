import string
import random

def password():

    pwd = ""
    limits  = [3, 3, 2]
    for i in range(len(limits)):
        delta = random.randint(1, limits[i] - 1)
        limits[i] -= delta
        limits[random.randint(0, len(limits) - 1)] += delta


    sources = [ string.ascii_lowercase,
                string.ascii_uppercase,
                string.digits + "_" ]

    while sum(limits) > 0:
        i = random.randint(0, len(limits)-1)

        if limits[i]:
            pwd += random.choice(sources[i])
            limits[i] -= 1

    return pwd

print(password())


# limits = [3, 3, 2]
# for i in range(len(limits)):
#     delta = random.randint(1, limits[i]-1)
#     limits[i] -= delta
#     limits[random.randint(0, len(limits)-1)] += delta