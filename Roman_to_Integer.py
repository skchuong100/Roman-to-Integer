#Create a functions where the numerals will be a divided
def div(roman1, roman2):
  return arabicToRoman(int(roman1/roman2))

#Create a function where the numerals will be multiplied
def mul(roman1, roman2):
  return arabicToRoman(roman1*roman2)

#Create a function where the numberals will be subtracted
def sub(roman1, roman2):
  #Create an if statement if the first roman numeral is bigger than the second roman numeral
  if roman1>roman2:
    return arabicToRoman(roman1-roman2)
  #Create a message if the second roman numeral is bigger than the first roman numeral
  else:
    return arabicToRoman(roman2-roman1)

#Create a function where the numerals will be added
def add(roman_word1, roman_word2): 
  return arabicToRoman(roman_word1+roman_word2)

#Create a function where the arabic number will be converted into a roman numeral
def arabicToRoman(arabic):
  #Create a list of values that matches the "symbol" list  
  arabic_number=[1, 4, 5, 9, 10, 40, 50, 90, 100]
  #Creata a list of roman numerals that matches the "number" list
  roman_symbol=["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C"]
  list_placement=8
  roman=""
  while arabic:
    #Create an equation have it go down the arabic_number list
    placement_in_list=arabic//arabic_number[list_placement]
    arabic%=arabic_number[list_placement]
    while placement_in_list:
      #Create an equation that will go down the roman_numeral list
      roman+=roman_symbol[list_placement]
      #Create an accumulator that will make the equation above go down
      placement_in_list-=1
    #Create an accumulator that will make the equation above go down
    list_placement-=1
  #Return value
  return roman

#Create a function that will convert a single roman numeral into its arabic numeral equivalent 
def letter_to_num(letter):
  if (letter=='I' or letter=='i'):
    return 1  
  elif (letter=='V' or letter=='v'):
    return 5
  elif (letter=='X' or letter=='x'):
    return 10 
  elif (letter=='L' or letter=='l'):     
    return 50
  elif (letter=='C' or letter=='c'):
    return 100
  return -1

#Create a function where the roman numeral inputted will be converted to its arabic numeral equivalent
def romanToArabic(roman):
  letter_list=[]
  i=0
  value_place=0
  total=0
  #Create an for loop  where it would count and loop the number of letters in the inputted roman numeral
  for x in range (len(roman)):
    #Create a while loop where it will loop until it reaches all the letters in the inputted roman numeral
    while i<len(roman):
      letter_list.append(roman[i])
      i+=1
  #Create a while loop so that it will continue to change the letter of a roman numeral into a value
  while value_place<len(letter_list):
    value1=letter_to_num(letter_list[value_place])
    if value_place+1<len(roman):
      #Create a variable where we assign the second value of an arabic number
      value2=letter_to_num(letter_list[value_place+1])
      #Create an if-else statement if the first value of a roman numeral is bigger than the value after it 
      if value1>=value2:
        total+=value1
        value_place+=1
      #Create an else statement if the second value that's after the first value is bigger than the first value
      else:
        total+=(value2-value1)
        value_place+=2
    else:
      total+=value1
      value_place+=2
  #Return the value of the function
  return total

#Create a function that will ask the user to input a second roman numeral
def getRomanN2():
  global numeral_input2
  #Ask the user to enter a second roman numeral
  numeral_input2=input('Enter Second Roman Number (no spaces): ')
  while not isValidRoman(numeral_input2):
    print("Invalid Roman Numeral")
    numeral_input2=input("Enter Second Roman Number (no spaces): ")
  #Return the roman numeral of what the user inputted
  return numeral_input2

#Create a function that will ask the user to input their first roman numeral
def getRomanN1():
  global numeral_input1
  #Ask the user to input their first roman numeral
  numeral_input1=input('Enter First Roman Number (no spaces): ')
  #is the isValidRoman function is false, then the while loop while start 
  while not isValidRoman(numeral_input1):
    #Display an error message
    print("Invalid Roman Number")
    #Ask the user again to input an roman numeral
    numeral_input1=input("Enter First Roman Number (no spaces): ")
  return numeral_input1

#Create a function that will check to see if the roman numeral that was inputtted is valid or not
def isValidRoman(roman):
  #Create a for loop
  for x in roman:
    #Create an if statement with a condition where if the roman numeral inputtted doesn't have an uppercase or lowercase C, X, L, I, and V, then it is invalid
    if x!='C' and x!='c' and x!='X' and x!='x' and x!='L' and x!='l' and x!='V' and x!='v' and x!='L' and x!='l' and x!='I' and x!='i':
      #Returns a False so it will activate the while loop in another function
      return False
  #Create an if statement to see if there are any invalid formatting of roman numerals
  if roman.count('IIII')!=0 or roman.count('iiii')!=0 or roman.count('XXXX')!=0 or roman.count('xxxx')!=0 or roman.count('CCCC')!=0 or roman.count('cccc')!=0 or roman.count('VV')!=0 or roman.count('vv')!=0 or roman.count('LL')!=0 or roman.count('ll')!=0 or roman.count('LC')!=0 or roman.count('lc')!=0 or roman.count('VX')!=0 or roman.count('vx')!=0 or roman.count('IL')!=0 or roman.count('il')!=0 or roman.count('IC')!=0 or roman.count('ic')!=0 or roman.count('XCX')!=0 or roman.count('xcx')!=0:
    #Returns a False so that it will activate the while loop in another function
    return False
  return True

#Create a function that will display a list of mathematical calculations, what it does, and what to put to end the program 
def menu():
  #Display information
  print('A - Add two Roman Numerals')
  print('S - Subtract two Roman Numerals')
  print('D - Divide teo Roman Numerals')
  print('Q - Quit')

#Create a main function
def main():
  x=True
  #Create a while loop that will only continue when x is True
  while x==True:
    #Display statement
    print('Welcome to the Roman Numerals Calculator')
    print('Please select from the following')
    print()
    menu()
    #Ask user to input what type of mathematical method to perform
    calc_type=input('Select A, S, M, D or Q only. ')
    #Create a while loop if to check to see if the inputted letter is valid and if not, the program will continue to ask the user until a valid letter is inputted
    while calc_type!='A' and calc_type!='a' and calc_type!='S' and calc_type!='s' and calc_type!='M' and calc_type!='m' and calc_type!='D' and calc_type!='d' and calc_type!='Q' and calc_type!='q':
      #Display error
      print()
      print('Invalid Entry. Please Try Again')
      print()
      print("Please select from the following:")
      print()
      menu()
      #Ask the user to input a valid letter
      calc_type=input('Select A, S, M, D or Q only. ')
    if calc_type=='A' or calc_type=='a':
      input_check1=romanToArabic(getRomanN1())
      print('Value of', numeral_input1, ":", input_check1)
      input_check2=romanToArabic(getRomanN2())
      print('Value of', numeral_input2, ":", input_check2)
      print(numeral_input1, '+', numeral_input2, "=", add(input_check1, input_check2))
      print(input_check1, "+", input_check2, '=', input_check1+input_check2)
      print()
      x=True

    elif calc_type=="S" or calc_type=='s':
      input_check1=romanToArabic(getRomanN1())
      print('Value of', numeral_input1, ":", input_check1)
      input_check2=romanToArabic(getRomanN2())
    
      print('Value of', numeral_input2, ":", input_check2)
      #Create an if statement if the difference is a positive number
      if input_check1>input_check2:
        print(numeral_input1, '-', numeral_input2, '=', sub(input_check1, input_check2))
      #Create a else statement if the difference is a negative number
      else:
        print(numeral_input1, '-', numeral_input2, '= -', sub(input_check1, input_check2))
      print(input_check1, '-', input_check2, '=', (input_check1-input_check2))
      print()
      x=True
    elif calc_type=="M" or calc_type=="m":
      input_check1=romanToArabic(getRomanN1())
      print('Value of', numeral_input1, ":", input_check1)
      input_check2=romanToArabic(getRomanN2())
      print('Value of', numeral_input2, ":", input_check2)
      print(numeral_input1, "*", numeral_input2, '=', mul(input_check1, input_check2))
      print(input_check1, 'x', input_check2, '=', (input_check1*input_check2))
      print()
      x=True

    elif calc_type=='D' or calc_type=='d':
      input_check1=romanToArabic(getRomanN1())
      #Display information
      print('Value of', numeral_input1, ":", input_check1) 
      input_check2=romanToArabic(getRomanN2())
      print('Value of', numeral_input2, ":", input_check2)
      if input_check1%input_check2==0:
        print(numeral_input1, "/", numeral_input2, '=', div(input_check1, input_check2), 'Remainder: None')
        print(input_check1, '/', input_check2, '=', input_check1//input_check2, 'Remainder: None')
      #Create an else statement if the quotient has a remainder or not
      else:
        print(numeral_input1, "/", numeral_input2, '=', div(input_check1, input_check2), 'Remainder:', arabicToRoman(input_check1%input_check2))
        print(input_check1, '/', input_check2, '=', input_check1//input_check2, 'Remainder:', input_check1%input_check2)
      print()
      x=True

    elif calc_type=='Q' or calc_type=='q':
      print('Good Bye.')
      x=False
      
#Call the main function
main()
