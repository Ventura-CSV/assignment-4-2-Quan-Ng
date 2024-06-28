def main():
    result = []
    a1 = int(input('Enter your first number: '))
    a2 = int(input('Enter your second number: '))
    N = int(input('Enter the number of sequences: '))
    result.append(a1)
    result.append(a2)
    """
    ########################################
    Code Your Program here
    ########################################
    """

        
    #generate sequnce
    for i in range(2,N):
        a3 = result[i-1] + result[i-2]
        result.append(a3)
        
        
    print(result)

    ########################################
    # Do not delete the return statement
    ########################################
    
    return result



if __name__ == '__main__':
    main()
