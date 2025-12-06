from tensorflow.python.tpu.tpu import split_compile_and_replicate

names = ["Blend","Florjon","Aldin","Ajan"]
for x in names:
    print(x)

sentence = "Hello, World!"

for ch in sentence:
    if ch.isalpha():
        print(ch)

for number in range(1,6):
    print(number)

numbers=[12,45,6,7,94]
max = numbers[0]

for num in numbers:
    if num > max:
        max = num
print('Maksimumi eshte:', max)

count = 1

while count<=5:
    print("Rrite vleren per 1:", count)
    count+=1

numbers = [1,2,3,4,5,6]
target=4

for number in numbers:
    print(number)
    if number == target:
        print("target found")
        break

scores=[68, 42, 57, 86, 73, 50, 92, 30]
total=0
count=0

for score in scores:
    if score<50:
        continue
    total+=score
    count+=1

mesatarja = total/count
print("Mesatarja ka qene:", mesatarja)

while True:
    user_input=input("Shtyp nje numer pozitiv:")
    if user_input.isnumeric():
        number = int(user_input)
        if number > 0:
            break
    print("Invalid. Try again")
print("You enter a positive number")

while True:
    user_input = input("Shkruaj një numër pozitiv çift: ")
    if user_input.isnumeric():
        number = int(user_input)
        if number % 2 == 0:
            break
    print("Invalid. Provoni përsëri.")
print("Keni futur një numër pozitiv çift!")

