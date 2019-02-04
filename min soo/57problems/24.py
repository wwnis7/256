print("Enter two strings and I'll tell you if they are anagrams: ")
def isAnagram(a,b):
    if len(a) == len(b):
        A = ''
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    A = A + a[i]
                    b = b[:j] + b[j+1:]
                    break
        print(a)
        print(A)
        if A == a:
            return True
        else:
            return False
    else:
        return False
a = input('Enter the first string: ')
b = input('Enter the second string: ')
D = {True:'', False:'not '}
print(f'"{a}" and "{b}" are {D[isAnagram(a.lower(), b.lower())]}anagrams')