if __name__ == '__main__':
    x = int(input('Enter the value of i: '))
    y = int(input('Enter the value of j: '))
    z = int(input('Enter the value of k: '))
    n = int(input('Enter the value of n: '))
    
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])