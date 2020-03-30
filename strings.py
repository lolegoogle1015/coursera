example_string = "Python course on Coursera"
print(example_string)

print(type(example_string))

example_string = "'Python course' on 'Coursera'"
print(example_string)

example_string = "\"Python\" course on \"Coursera\""
print(example_string)

#r-strings
example_string = "A file on disk c:\\\\"
print(example_string)

example_string = r"A file on disk c:\\"
print(example_string)

#How to split long strings

example_string = "Perl - is the language, which looks the same"\
                 " as before and after RSA encoding"\
                 "(c)Keith Bostic"
print(example_string)

example_string = """
Є всього два типи мов програмування: ті,
 на які люди все одно сварться, та ті, які ніхто не використовує.

 Bjarne Strustrup
 """
print(example_string)

dot = '.'
example_string = example_string + dot
print(example_string)

print(dot*3)

#Strings can`t be chanched
example_string = "Hi"
print(id(example_string))
example_string = "Oh hi, Mark!"
print(id(example_string))
#output:
#139828251348696
#139828226371632
#The 2 different Strings

example_string = "Python course on Coursera"
print(example_string[9:])#start
print(example_string[9:15])#start:stop
print(example_string[-9:])#start
print(example_string[::2])#start:stop:step
#invert string
print(example_string[::-1])
