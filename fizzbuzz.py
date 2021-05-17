""" FizzBuzz!

Prints the Fizz Buzz sequence up to a given number.

Authored by: Section 371 of Code in Place
Contributors:
* Jay
* Jay No.2
"""

def main():
    # ask the user for input, as a string
    user_number_str = input("Enter a number to count to: ")

    # transform the string into an integer
    user_number = int(user_number_str)

    # repeat the indented code below as many times as the user number
    for i in range(1, user_number+1):
        
        # check whether the current number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        # check whether the current number is divisible by 3
        elif i % 3 == 0: 
            print("fizz")
        # check whether the current number is divisible by 5
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

 
if __name__ == '__main__':
    main()
