# TODO Найдите количество книг, которое можно разместить на дискете

V_size = 1.44 * 1024 * 1024
n_str = 100
n_cnt = 50
n_numbers = 25
byte = 4

size_book = n_str * n_cnt * n_numbers * byte

count = V_size // size_book

print("Количество книг, помещающихся на дискету:", int(count))
