def fizzBuzz():

  tempList = []

  for x in range(1, 16):
    word = ""
    if (x%3 == 0 or x%5 == 0):
      if (x%3 == 0):
        word = "fizz"
      if (x%5 == 0):
        word = "buzz"
      if (x%3 == 0 and x%5 == 0):
        word = "fizzbuzz"
    else:
      word = x

    tempList.append(word)

  return tempList


