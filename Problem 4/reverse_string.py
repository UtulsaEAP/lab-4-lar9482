"""
Complete the following python code to reverse the string entered by the user.

Name: Luke Runnels
Lab Time: 2/16/2024
"""

def reverse_string():
    # YOUR CODE HERE
    inputString = input()
    while (inputString != 'Done' and inputString != 'done' and inputString != 'd'):
        reverse_string = ''
        for i in range(len(inputString)-1, -1, -1):
            reverse_string += inputString[i]
        
        print(reverse_string)
        inputString = input()

if __name__ == "__main__":
    reverse_string()