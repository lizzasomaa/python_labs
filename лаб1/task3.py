pages = 100
str_on_page = 50
sym_on_str = 25
memory_into_bytes = (int)(1.44 * 1024 * 1024)

total_sym = sym_on_str * str_on_page * pages
total_bytes = total_sym * 4

print("Количество книг, помещающихся на дискету:", memory_into_bytes // total_bytes)
