keys=['a', 'b', 'c', 'd']
values=[1, 2, 3, 4]
dictionary = {v: k for k, v in zip(keys, values)}
print(dictionary)