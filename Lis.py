def verify_subseq(seq, subseq):
    """
    param seq: a list of a sequence
    param subseq: a list of a sequence
    Determines whether subseq is a subsequence of seq
    Returns: A bool value
    """
    index = 0  #create a variable that tracks the current index
    for element in subseq:
        truth =  False
        while index < len(seq):
            if seq[index] == element:
                truth = True
                break
            #if the element is found in the main sequence, move on to next 
            #element
            index += 1
        if not truth:
            return False
        #if element in subsequence not found in main sequence, return false
    return True


def verify_increasing(seq):
    """
    param seq: a list of a sequence
    Determines whether the elements in seq are in ascending order
    Returns: a bool value
    """
    num = len(seq) - 1    
    for i in range(num):
        if seq[i] < seq[i+1]:
            continue
        else:
            return False
        #checks if the next value is greater than the current value
    return True


def find_lis(seq):
    """
    param seq: a list of a sequence
    Finds the longest increasing subsequence of seq
    Returns: A list of the longest increasing subsequence of seq
    """
    M, N = [], []
    num = len(seq)
    
    for i in range(num):
        M.append(0)
        N.append(0)
        
    #create a column and row list of a matrix to keep track of sequence
        
    length = 1  #default length of sequence is 1
  
    for i in range(1, num):
        
        l_bound = 0 
        u_bound = length
        
        #the bounds for a binary search tree

        
        if seq[M[u_bound-1]] < seq[i]:
            index = u_bound
            
        #if the last value in the sequence is greater thant the current item,
        #the last value is the key index

        else:
            #binary search
            while l_bound < u_bound - 1: 
                mid = (u_bound + l_bound) // 2
                #finds the midpoint 
                if seq[M[mid-1]] < seq[i]:
                    l_bound = mid
                else:
                    u_bound = mid
                #adjust the midpoint based on comparison of current item and
                #item in current subsequence

            index = l_bound    #key index if lower bound

        N[i] = M[index-1] 

        if index == length or seq[i] < seq[M[index]]:
            M[index] = i 
            #adjust the index of the sequence
            if index+1 > length:
                length = index+1
            #length of the subsequence increases

    
    lis = []
    for j in range(length):
        lis.append(0)
    #create main list
        
    item = M[length-1] #first item in subsequence is last item in M
    for k in range(length):        
        lis[k] = seq[item] 
        item = N[item]
        #add elements of the subsequence to main list

    lis = list(reversed(lis)) #reverse the list

    return lis    
            
                
