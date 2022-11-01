# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.
i = 0
while i < 50:
  if i == 0:  
    number = 0
  elif i == 1:
    number = 1
    prev = 0
  else:
    new_number = prev + number
    prev = number
    number = new_number
  print((f'term: {i} / number: {number}'))
  i += 1

# Hint: The next number is found by adding the two numbers before it