str1 = 'AAA BBBB CCCC dddd'
print(f'\nNapis: {str1} jest typu {type(str1)} i ma dlugosc {len(str1)}')
print(f', jego metody to m.in.: {dir(str1)[0:4]}')

print('Karol powiedział "Dziekuje" \n')

# dlugie napisy; """ wykorzystuje się też w docstrings:
print('dlugi napis, a dzieki znakowi \
    napisac w 2 liniach, a wydrukuje sie w jednej \n')
print("""a tu inne podejscie: 
        dlugi napis, ktory moge  
       napisac w 3 liniach i wydrukuje sie w 3""")

s1, s2 = 'to', 'napis'
s3 = s1 + ' ' +s2
print(f'\n{s1} + {s2} = {s3},  a s3[-1] to {s3[-1]} \n')

str_4slice = '012345678'
print(f'dla napisu {str_4slice} [0:3] to {str_4slice[0:3]}')
print(f'dla napisu {str_4slice} [:5] to {str_4slice[:5]}')
print(f'dla napisu {str_4slice} [5:] to {str_4slice[5:]}')
print(f'dla napisu {str_4slice} [:] to {str_4slice[:]}')
print(f'dla napisu {str_4slice} [:14] to {str_4slice[:14]}')
print(f'dla napisu {str_4slice} [13:15] to {str_4slice[13:15]} czyli pusty ciag')
print(f'dla napisu {str_4slice} [-9:-6] to {str_4slice[-9:-6]}')
print(f'dla napisu {str_4slice} [1:1] to {str_4slice[1:1]}')
print(f'dla napisu {str_4slice} [-9:0] to {str_4slice[-9:0]}')
print(f'dla napisu {str_4slice} [-9:] to {str_4slice[-9:]}')
print(f'bazinga => zinga :: {"bazinga"[2:]}')

# s2[0] = 'z'  # Error :: Strings Are Immutable
s2 = 'z' + s2[1:]
print(f'\n"Nowy" s2 = {s2}')

name = " Jean-luc Picard   "
print(name, name.lower(), name.upper())
print("Immutability::", name, name.lower(), name)
print(name.rstrip(), name.lstrip(), name.strip())  # Removing Whitespace

starship = "Enterprise"
print(starship.startswith("En"))
print(starship.endswith("risE"))

# user_input = input('Wybierz opcję (1..5) ')
# print("Wybrałeś: ", user_input)
# print(type(user_input))

print("'12' * 3 to:", '12' * 3)
print('')
print(int(12), float(12.1), '//', str(10 - 5), type(str(10 - 5)))

print(str(print), str(int), str(float))
# '<built-in function print>' "<class 'int'>" "<class 'float'>"

