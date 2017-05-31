def palindromecheck(palindrome):
    if len(palindrome)<=1:
        return True
    elif palindrome[0]==palindrome[len(palindrome)-1]:
        print palindrome[0:(len(palindrome)-1)]
        return palindromecheck(palindrome[1:(len(palindrome)-1)])
    else:
        return False