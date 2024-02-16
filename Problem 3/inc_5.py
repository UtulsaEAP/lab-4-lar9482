"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Luke Runnels
Lab Time: 2/16/2024
"""

def inc_5():
    # Write your code here
    lowerBound = int(input())
    upperBound = int(input())
    if (lowerBound > upperBound):
        print("Second integer can't be less than the first.")
        return
    
    output = ""
    for i in range(lowerBound, upperBound+5, 5):
        output += "{0} ".format(i)
    
    print(output)



if __name__ == '__main__':
    inc_5()