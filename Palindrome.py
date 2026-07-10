def palindrome(num):

    reverse = num[::-1]

    number = (int)(num)

    reverse = (int)(reverse)

    if(reverse == number):

        print("Palindrome number",number)

    else:

        print("Not Palindrome",number)


num = input()


palindrome(num)



    

