# ************** types of errors *****************


# a = int(input("Enter your number: "))   # input from the user
# c = 1/a
# print(c)       # in the input if user enters string instead of integer then it will throw an error and further process will not print, means the code will exit from here <-- this line.it will not go below.so for that we will not get the below print statement. to avoid this we use the try method.

# print("Thanks for using this code!")


# in the above code if i not write the integer then it will throw an error. below print statement will not print, means that where errors occurs from there the code will not execute below.
# to avoid this we use the 'try method'.see below example.





# *************** Exception ******************

# try:
#     a = int(input("Enter your number: "))    # input from the user.
#     c = 1/a
#     print(c)    # if error occurs then also it will the hole code, means it will go below to execute the below print statement.

# except Exception as a:    # if error occurs then this line will show the error.
#     print("Error is: ", a)

# print("Thanks for using this code!")






# ******** valueerror/ZeroDivisionError ********************



try:
    a = int(input("Enter your number: "))  
    c = 1/a 
    print(c)


# if i not writen this below method then if the user enters other than integer then the further code will not execute.means the code will exit.
except ValueError as a:      # prints the error when input other than integer like if string or any other.
    # print("Error is: ", a)   # showing the error to the user with the help of 'a'.
    print("Please enter the valid number! ")     # not showing the error to the user. what will the user will do.


# if the below method is not write then when user gives the input '0' then it willl throw an error,means the code will exit and further print statement will not print, to avoid this we use this, when the user enters '0' as input then print statement will print except ZeroDivisionError as a:    # prints the error when input is 0, means when the user gives the input as 0 then this <-- will execute.      
except ZeroDivisionError as a:
    print("0 is not allowed.")

print("Thanks for using this code!")


#datta kale





