from cgi import print_directory


conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b)) # tem no conjunto 'a' e não tem no conjunto 'b'
print(conjunto_b.difference(conjunto_a)) # tem no conjunto 'b' e não tem no conjunto 'a'