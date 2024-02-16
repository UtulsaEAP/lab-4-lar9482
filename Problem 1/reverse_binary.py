"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Luke Runnels
Lab Time: 2/16/2024

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE
    binary_num = ""
    while (user_num > 0):
        binary_num += str(user_num % 2)
        user_num = user_num // 2
    
    print(binary_num)

if __name__ == "__main__":
    reverse_binary()