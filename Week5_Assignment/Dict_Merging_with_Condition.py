Dict1={'a':20, 'b':3, 'c':1, 'd':88, 'f':55, 'g':92, 'h':6, 'e':90, 'a':910}
Dict2={'u':200, 'b':30, 'o':10, 'x':88, 'e':55, 'a':920}

merged_dict = {**{k: v for k, v in zip(Dict1.keys(), Dict1.values()) if v % 2 != 0 }, 
               **{k: v for k, v in zip(Dict2.keys(), Dict2.values()) if v % 2 != 0 }}
print(merged_dict)
 