# -*- coding: utf-8 -*-
I = 1
J = 7
while True:
    if I <= 9 or J <= 5:
        if J >= 5:
            print("I=%d J=%d" % (I, J))
            J -= 1
        else:
            J = 7
            I += 2
    else:
        break