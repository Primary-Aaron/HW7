def fizzBuzz(num):
  word = ""
  if (num%3 == 0):
    word = word + "fizz"
  if (num%5 == 0):
    word = word + "buzz"
  else:
    word = num

  return word


