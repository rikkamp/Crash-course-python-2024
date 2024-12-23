x = 'hello'
y = "hello"

print(x == y)
print(x != y)
x = 'hello'
y = "heLLo"
print(x == y)
print(x != y)

a = "a" # value of 97
z = "Z" # value of 90

print(a < z)

# The greater or less than is based on the ASCII value of the characters
print(ord(a), ord(z))

result = 6 == 6
print(result)

x = 7
y = 8
z = 0

result1 = x == y # false
result2 = y > x # true
result3 = z < x + 2 # false

print(not True) # false
print(result1 or result2 or result3) # true if 1 is true
print(result1 or result2 and result3) # result1 true otherwise result2 and 3 should be true