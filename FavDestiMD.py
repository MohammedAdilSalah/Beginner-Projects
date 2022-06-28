def madlib():
 print ("------I am Superhero------")
 w1 = input("Name your dream destination: ")
 w2 = input(f"Why do you want to visit {w1}: ")
 w3 = input("How will you reach your destination: ")
 w4 = input("Whom other will you take with you: ")
 madlib_final = f"I would like to visit {w1}. {w1} is my favourite place.\
 The reason I like this place so much is because {w2}. I will travel to {w1} By {w3}. I want to enjoy this trip with {w4}"
 print(madlib_final)
 
madlib()