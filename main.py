print("This program will take the two numbers that is inputted and will print it out in the reverse order (also tons of other random things)") # Explains what the program does 
try: # Catches + handles exceptions
  x, y = int(input("Please enter a number: ")), int(input("Please enter a number: ")) # Declares the x and y values equal to what the user inputs 
  x = x + y # Adds the first number to the third number 
  y = x - y # Subtracts the first number by the third number to get the first number
  x = x - y # Subtracts the first number by the third number to get the third number

  print("reversed: %s" %x, y) # Prints out the two numbers that have been reversed 

except Exception as e: # Declares variable e as the exception 
  print(e) # Prints out the exception 