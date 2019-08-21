def silly():
    res = []
    done = False
    while not done:
        elem = input('Enter element. Return when done. ')
        if elem == "":
            done = True
        else:
            res.append(elem)
    tmp = res[:] #Important to write [:] as it indicates that we want tmp to be
                 #a copy of the LIST res, not refer back to res. CLoning rather than
                 #assignment.
    tmp.reverse()
    isPal = (res == tmp)
    if isPal:
        print('is a palindrome')
    else:
        print('is NOT a palindrome')

silly()
