first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(string) for string in first_strings if len(string) >= 5]
second_result = [(str1, str2) for str1 in first_strings for str2 in second_strings if len(str1) == len(str2)]
str = first_strings + second_strings
third_result = {st1: len(st1) for st1 in str if len(st1) % 2 == 0}
# print(str)

# print(len(first_strings[2]))
print(first_result)
print(second_result)
print(third_result)