# -*- coding: utf-8 -*-
I = 1
J = 7
MaxJ = 7
while True:
    if I <= 9 or J == 13:
        if J >= MaxJ-2:
            print("I=%d J=%d" % (I, J))
            J -= 1
        else:
            MaxJ += 2
            I += 2
            J = MaxJ
    else:
        break