#!/usr/bin/python3
def common_elements(set_1, set_2):
    for x in set_1:
        for i in set_2:
            if x == i:
                return x
        return(set_1 & set_2)
