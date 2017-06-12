# -*- coding: utf-8 -*-
Z = 0
Z = float(Z)
while Z <= 2.0:
    for x in range(1, 4):
        if Z == 1.9999999999999998:
            print("I=%d J=%.1f" % (2, float(x) + Z))
        elif Z == 1.0:
                print("I=%d J=%.1f" % (1, float(x) + Z))
        elif Z == 0.0:
            print("I=%d J=%.1f" % (0, float(x) + Z))
        else:
            print("I=%.1f J=%.1f" % (Z, float(x)+Z))
    Z += 0.2