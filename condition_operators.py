company = "my.com"
if "my" in company or company.endswith(".com"):
    print("Condition is completed")

company = "google.com"
if "my" in company:
    print("Умова виконана!")
else:
    print("Умова не виконана!")

company = "google.com"
if "my" in company:
    print("Підстрічка не знайдена")
elif "google" in company:
    print("Підстрічка google знайдена")
else:
    print("Підстрічка не знайдена!")

#Тернарний оператор

score_1 = 5
score_2 = 0
winner = "Argentina" if score_1 > score_2 else "Jamaica"
print(winner)

#while

i = 0

while i<100:
    i +=1

print(i)

#for_in

name = "Alex"
for letter in name:
    print(letter)

for i in range(3):
    print(i)

result = 0

for i in range(101):
    result += i
print(result)

for i in range(5,8):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10, 5, -1):
    print(i)
