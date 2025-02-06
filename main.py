def add (numbers):
    delimiter = ','
    result = 0
    if numbers == '' :  return result

    if '//' in numbers:
        delimiter = numbers[2:3]

    numbers = numbers.replace("\\n", "").replace("\n", "").replace("//"+delimiter, "")
    numbers_list = numbers.split(delimiter)
    for number in numbers_list:
        if int(number) < 0:
            raise Exception("negative number not allowed "+str(number))
        result = result + int(number)
    return result

# print ("Please enter input series of numbers")
# numbers = input()

# try:
#     results = add(numbers)
#     print ("Sum of All numbers : " + str(results))
# except Exception as e:
#     print(e)


    