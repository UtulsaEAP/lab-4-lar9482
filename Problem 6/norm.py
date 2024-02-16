"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Luke Runnels
Lab Time: 2/16/2024
"""

def norm():
    # Write your code here
    numDataset = int(input())
    dataset = []
    
    maxNum = -10000000
    for i in range(0, numDataset):
        newNum = float(input())
        maxNum = max(maxNum, newNum)
        dataset.append(newNum)

    for i in range(0, numDataset):
        normalizedNum = dataset[i] / maxNum
        print(f'{normalizedNum:.2f}')


    


if __name__ == "__main__":
    norm()