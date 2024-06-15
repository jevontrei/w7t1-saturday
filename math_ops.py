
# Using *args
def add(*args):
    sum = 0
    for each in args:
        sum += each
    return sum


def subtract(*args):
    difference = 0
    for each in args:
        difference -= each
    return difference


def multiply(*args):
    # Must initialise as 1, not 0:
    product = 1
    for each in args:
        product *= each
    return product


# def divide(*args):
#     # Must initialise as 1, not 0:
#     quotient = 1
#     for each in args:
#         if each != 0:
#             quotient /= each
#     return quotient

print(add(5, 6, 4, 88))