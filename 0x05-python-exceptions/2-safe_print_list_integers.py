#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(x):
        item = my_list[i]
        try:
            print("{:d}".format(item, end="")
            counter += 1
        except Exception:
            continue                                                               
    print("") 
    return counter
