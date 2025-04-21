listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
power2s = [2, 4, 8, 16]
def numberGuesser():
    userNumber = 0
    
    evenOdd = input('Even or Odd?')

    #removes any spaces and capitalizes the first letter, and lowercases the rest.
    evenOdd = evenOdd.replace(" ", "")
    evenOdd = evenOdd.capitalize()

    if (evenOdd == 'Even'):
        indexValue = len(listOfNumbers)

        while indexValue > 0:

            if (listOfNumbers[indexValue - 1] % 2 == 1):
                listOfNumbers.pop(indexValue - 1)
            indexValue = indexValue - 1

        print (f'Remaining Numbers {listOfNumbers}')

        powerOf2 = input('Can the value be obtained by a power of 2?')
        
        powerOf2 = powerOf2.capitalize()
        powerOf2 = powerOf2.replace(" ", "")

        if powerOf2 == 'Yes':
            indexValue = len(listOfNumbers)
            
            while indexValue > 0:
                if listOfNumbers[indexValue - 1] in power2s:
                    indexValue = indexValue - 1

                else:
                    listOfNumbers.pop(indexValue - 1)
                    indexValue = indexValue - 1
                
        elif powerOf2 == 'No':
            indexValue = len(listOfNumbers)

            while indexValue > 0:
                if listOfNumbers[indexValue - 1] in power2s:
                    listOfNumbers.pop(indexValue - 1)
                  
                indexValue = indexValue - 1
        print(f'Remaining Numbers {listOfNumbers}')

        equationQuestion = input('Now, add 23, multiple by 4, and subtract 5 from your number. What is your number?')
        equationQuestion = int(equationQuestion)

        finalGuess = ((equationQuestion + 5) // 4) - 23
        
        print(f'Your number is {finalGuess}')
    elif (evenOdd == 'Odd'):
        indexValue = len(listOfNumbers)

        while indexValue > 0:
            if (listOfNumbers[indexValue - 1] % 2 == 0):
                listOfNumbers.pop(indexValue - 1)
            
            indexValue = indexValue - 1
           
        print(f'Remaining Numbers {listOfNumbers}')
        multipleOf3 = input('Is your number a multiple of 3?')

        multipleOf3 = multipleOf3.capitalize()
        multipleOf3 = multipleOf3.replace(" ", "")

        if multipleOf3 == 'Yes':
            indexValue = len(listOfNumbers)

            while indexValue > 0:
                if listOfNumbers[indexValue - 1] % 3 > 0:
                    listOfNumbers.pop(indexValue - 1)
                indexValue = indexValue - 1
        
        if multipleOf3 == 'No':
            indexValue = len(listOfNumbers)

            while indexValue > 0:
                if listOfNumbers[indexValue - 1] % 3 == 0:
                    listOfNumbers.pop(indexValue - 1)
                indexValue = indexValue - 1
        print (f'Remaining Numbers {listOfNumbers}')

        quotientQuestion = input('What is the quotient of the number when divided by 2? (type only whole numbers, round down if needed)')
        quotientQuestion = int(quotientQuestion)

        finalGuess = 2 * quotientQuestion + 1

        print(f'Your number is {finalGuess}')
    else:
        print('Invalid Response, please specify even or odd.')
        numberGuesser()

    
print('Choose a number between 1-25, and answer the questions that follow!')
numberGuesser()

