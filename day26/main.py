# List comprehensions

with open("file1.txt") as file1:
     file1_content = file1.read()
     file1_list = [int(x) for x in file1_content.splitlines()]

with open("file2.txt") as file2:
    file2_content = file2.read()
    file2_list = [int(x) for x in file2_content.splitlines()]

tuple1 = tuple(file1_list)
tuple2 = tuple(file2_list)
print(tuple1, tuple2)

result = [x for x in tuple1 if x in tuple2]
#print(result)
# Dictionary  comprehension

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
new_sentence = sentence.replace(" ", ",").split(",")
result = {word:len(word) for word in new_sentence}
print(result)