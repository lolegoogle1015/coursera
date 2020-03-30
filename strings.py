#String Methods
quote = """Болтовня ничего не стоит. Покажите мне код.

Linus Torvalds
"""
print(quote.count("o"))

print("ukraine".capitalize())

print("2020".isdigit())

#"in" operator

print("3.14" in "Pi number = 3.1415926")

print("Oleh" in "Andriy")

#"for in"
example_string = "Hi"
for letter in example_string:
    print("Letter", letter)

str = bool("asdad")
print(str)

#Strings formating
template = "%s - головна перевага програміста. (%s)(%d)" % ("Лінь", "Larry Wall",190)
print(template)

print("{} не брешуть, але {} користуються формулами. ({})".format("Цифри", "Брехуни", "Robert A.Heinlein"))
print("{num} не брешуть, але {people} користуються формулами. ({author})".format(num="Цифри", people="Брехуни", author="Robert A.Heinlein"))

#f-strings Python3.6

subject = "optimization"
author = "Donald Knuth"

print(f"Передчасна {subject} - корінь всіх бід. ({author})")

num = 8
print(f"Binary: {num:#b}")

num = 2/3
print(num)

print(f"{num:.3f}")
