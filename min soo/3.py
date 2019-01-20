# def quote(a, b):
#     print(b + f' says, "{a}".')
# quote(input('What is the quote?'), input('Who said it?'))

quote = lambda a, b: print(b + f' says, "{a}".')
quote(input('What is the quote?'), input('Who said it?'))