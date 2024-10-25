# TODO Найдите количество книг, которое можно разместить на дискете
sizeall_in_megabytes = 1.44
pages = 100  # кол-во страниц
lines_in_page = 50  # кол-во строк
simvols_in_line = 25  # кол-во символов
size_one_simvol = 4  # размер 1 символа
number_of_simvols = pages * lines_in_page * simvols_in_line
size_all_simvols = size_one_simvol * number_of_simvols
size_in_megabytes = size_all_simvols / 1024 / 1024
number_of_books = sizeall_in_megabytes / size_in_megabytes
print("Количество книг, помещающихся на дискету:", int(number_of_books))
