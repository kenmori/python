start =  'hello' *4 + "\n"
middle = '!' * 10 + '\n'
end = 'python world'
print(start + middle + end)


str = '2 no 3 jouha 8'[-1]
print(str)  #2


str2 = 'user-111@example.com'
print(str2[9:])
# example.com

print(str2[-3:])
# com

print(str2[:])
# user-111@example.com

print(str2[:0])
# empty

print(str2[:1])
# u  #index -1 wo hiku = 0

print(str2[:8])
# user-111

