def fizzBuzz():

  tempList = []

  for x in range(1, 100):
    word = ""
    
    if (x%3 == 0):
      word = word + "fizz"
    if (x%5 == 0):
      word = word + "buzz"
    else:
      word = x

    tempList.append(word)

  return tempList


