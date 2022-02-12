# Arranging Books
from collections import Counter
books = input()

bookCount = dict(Counter(books))

LSmall = 0
LMedium = 0

MLarge = 0
MSmall = 0

SLarge = 0
SMedium = 0

if 'M' in books:
    for i in range(bookCount['L']):
        if books[i]=='S':
            LSmall += 1
            continue
        if books[i]=='M':
            LMedium += 1

    for i in range(bookCount['L'], bookCount['L']+bookCount['M']):
        if books[i] =='S':
            MSmall += 1
            continue
        if books[i]=='L':
            MLarge += 1

    for i in range(bookCount['L']+bookCount['M'], len(books)):
        if books[i] =='M':
            SMedium += 1
            continue
        if books[i] =='L':
            SLarge += 1

    misplaces = LSmall+LMedium+MSmall+MLarge+SMedium+SLarge

    if LSmall >= SLarge:
        moves=LSmall+MLarge+MSmall
    else:
        moves=SLarge+MSmall+MLarge
    
    print(moves)
else:
    if 'L' in books:
        for i in range(bookCount['L'],len(books)):
            if books[i]=='L':
                SLarge += 1
        print(int(SLarge))
    else:
        print(0)