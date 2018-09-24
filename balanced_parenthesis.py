n = 8


def all_parenthesis_combinations(x):
    next_parenthesis_combination = ''
    for i in range(2**x):
        for j in range(x):
            if i & 1:
                next_parenthesis_combination += str('(')
            else:
                next_parenthesis_combination += str(')')
            i = i >> 1
        yield next_parenthesis_combination
        next_parenthesis_combination = ''


def check_balanced(x):
    balanced = True
    count_opened = 0
    for i in x:
        if i == '(':
            count_opened += 1
        else:
            count_opened -= 1
        if count_opened < 0:
            balanced = False
    if count_opened != 0:
        balanced = False
    return balanced


def balanced_parenthesis_combinations(x):
    balanced_combinations = []
    if (x/2 != x//2) or (x < 2):
        return balanced_combinations
    for i in all_parenthesis_combinations(x):
        if check_balanced(i):
            balanced_combinations.append(i)
    return balanced_combinations


print(balanced_parenthesis_combinations(n))
