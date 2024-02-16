"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Luke Runnels
Lab Time: 2/16/2024
"""

def password_mod():
    word = input()
    password = ''
    # Type your code here.

    for i in range(0, len(word)):
        if (word[i] == 'i'):
            password += '1'
        elif (word[i] == 'a'):
            password += '@'
        elif (word[i] == 'm'):
            password += 'M'
        elif (word[i] == 'B'):
            password += '8'
        elif (word[i] == 's'):
            password += '$'
        else:
            password += word[i]
    password += '!'
    print(password)

if __name__ == "__main__":
    password_mod()