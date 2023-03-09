# python3
import math
def build_heap(data):
    swaps = []
    doublecheck=[]
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    size=len(data)
    for i in reversed(range(math.floor((len(data)+1)/2))):
        left=i*2+1
        right=i*2+2
        notFound=True
        if left<size and data[left]<data[i]:
            smallest = left
            notFound=False
        if right<size and data[right]<data[i] and data[right]<data[left]:
            smallest = right
            notFound=False
        if notFound:
            continue
        swap1=data[i]
        swap2=data[smallest]
        data[i]=swap2
        data[smallest]=swap1
        swaps.append([i, smallest])
        doublecheck.append(smallest)
    # Re-check swapped elements
    while len(doublecheck)!=0:
        k=doublecheck[0]
        del doublecheck[0]
        if k>math.floor((len(data)+1)/2):
            continue
        left=k*2+1
        right=k*2+2
        notFound=True
        if left<size and data[left]<data[k]:
            smallest = left
            notFound=False
        if right<size and data[right]<data[k] and data[right]<data[left]:
            smallest = right
            notFound=False
        if notFound:
            continue
        swap1=data[k]
        swap2=data[smallest]
        data[k]=swap2
        data[smallest]=swap1
        swaps.append([k, smallest])
        doublecheck.append(smallest)
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    entry=input()
    if entry[0]=="I":
        n=input()
        data=list(map(int, input().split()))
    elif entry[0]=="F":
        filename=input()
        file=open(str("tests/"+filename), "r")
        n=int(file.readline())
        data = list(map(int, file.readline().split()))
    else:
        print("Error!\nInput I for manual input or F to read from file")

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
