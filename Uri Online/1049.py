# -*- coding: utf-8 -*-
V1 = input()
V2 = input()
V3 = input()
if V1 == "vertebrado" and V2 == "ave" and V3 == "carnivoro":
    print("aguia")
elif V1 == "vertebrado" and V2 == "ave" and V3 == "onivoro":
    print("pomba")
elif V1 == "vertebrado" and V2 == "mamifero" and V3 == "onivoro":
    print("homem")
elif V1 == "vertebrado" and V2 == "mamifero" and V3 == "herbivoro":
    print("vaca")
elif V1 == "invertebrado" and V2 == "inseto" and V3 == "hematofago":
    print("pulga")
elif V1 == "invertebrado" and V2 == "inseto" and V3 == "herbivoro":
    print("lagarta")
elif V1 == "invertebrado" and V2 == "anelideo" and V3 == "hematofago":
    print("sanguessuga")
else:
    print("minhoca")