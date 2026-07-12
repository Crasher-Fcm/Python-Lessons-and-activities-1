test_dict = {'Learn' : 5, 'coding' : 5, 'in' : 5, 'Codingal' : 5, 'best' : 5}

print("The original dictionary is : " + str(test_dict))


P = 5
res = 0
for key in test_dict:
    if test_dict[key] == P:
        res = res + 1

print("The frequency of P is : " + str(res))