def decimal_to_binary(num):
    binaryNum = ''
    if num == 0:
        return 0
        #in case the number entered is 0, the value is returned as 0
    while num > 0:
        #to find the binary number, we divide the number by 2 to find the remaider. the remainder gives us a 1 or 0. we then repeat the process till number = 0
        temp = num % 2
        num = num // 2
        binaryNum = str(temp) + binaryNum 
    return binaryNum

def binary_to_decimal(binaryNum):
    #setting loopTimes = to the length of the string so we can keep track of what power we are multiplying by.
    loopTimes = len(binaryNum) - 1
    #temp value will be used to determine the position we are in for the string in the while loop.
    temp = 0
    decimalValue = 0
    while loopTimes > 0:
        if (binaryNum[temp] == '1'):
            decimalValue = pow(2, loopTimes) + decimalValue
        loopTimes = loopTimes - 1
        temp = temp + 1
    return decimalValue

return_value = input('Is this Binary or Decimal? ')

#determine if it is decimal or binary, then converts to string or integers to prevent errors with the function.B
if (return_value == 'Decimal' or return_value == 'decimal'):
    user_input = input('Please input your decimal value ')
    user_input = int(user_input)
    x = decimal_to_binary(user_input)
    print(f'the binary representation of {user_input} is {x}.')

elif (return_value == 'Binary' or return_value == 'binary'):
    user_input = input('Please input your binary value ')
    user_input = str(user_input)
    y = binary_to_decimal(user_input)
    print(f'the decimal representation of {user_input} is {y}.')
#if the value is anything other than binary or decimal, it will return nothing but to tell them to retry.
else:
    print('Please Enter in Binary or Decimal for this to work.')