# TODO Найдите количество книг, которое можно разместить на дискете
sizeall = 1.44
sta = 100 #кол-во страниц
stra = 50 #кол-во строк
sim = 25 #кол-во символов
size1sim = 4
kolsim = sta * stra * sim
sizesimvolov = size1sim * kolsim
amb = sizesimvolov / 1024 / 1024
v = sizeall / amb
print("Количество книг, помещающихся на дискету:", round(v))
