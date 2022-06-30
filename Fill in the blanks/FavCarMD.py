def madlib():
 print ("------My Fav Car------")
 w1 = input("What is your favourite car: ")
 w2 = input("What coluor would you match your car with: ")
 w3 = input("Feature that made you like the car: ")
 w4 = input("With whom will you share a long drive in the car: ")
 madlib_final = f"{w1} is my favourite car. I would choose a {w2} colour {w1}.\
I like this car because of its {w3}. This car has got all that needs to satisfy my drive cravings.\
I would take my {w4} for a long trip in my{w1}."
 print(madlib_final)
 
madlib()