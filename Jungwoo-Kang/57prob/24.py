def anagram(a, b):
    if set(a)==set(b) and len(a)==len(b):
        print(f'"{a}" and "{b}" are anagrams.')
    else:
        print(f'"{a}" and "{b}" are not anagrams.')


word1, word2 = input('''Enter two strings and I'll tell you if they are anagrams:''').split(',')

anagram(word1,word2)
