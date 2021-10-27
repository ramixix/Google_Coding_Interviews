
'''
Task 1 RemoveIslands :
info :  Imagine that you have an black and white image. As you know every image is contructed from 
        small parts called pixel. So here our image pixel are either black or white. Let's say that number 1 
        represent pixels that are black and 0 represend pixels that are white. (think image as 2 dimensional array)

        for example our image might be like:
            [1, 0, 0, 0, 0, 0]
            [0, 1, 0, 1, 1, 1]
            [0, 0, 1, 0, 1, 0]
            [1, 1, 0, 0, 1, 0]
            [1, 0, 1, 1, 0, 0]
            [1, 0, 0, 0, 0, 1]
        
        Now Your task is to remove all black pixels that are not connected to the border ( note: if a black pixels be vertically or horizontally 
        conneted to other black pixels that are connected to borther should not get removed)

        for example :
            [1, 0, 0, 0, 0, 0]                              [1, 0, 0, 0, 0, 0]                                  [ ,  ,  ,  ,  ,  ]
            [0, 1, 0, 1, 1, 1]                              [0, 0, 0, 1, 1, 1]                                  [ , 1,  ,  ,  ,  ]
            [0, 0, 1, 0, 1, 0]         after operation      [0, 0, 0, 0, 1, 0]      the ones that get removed   [ ,  , 1,  ,  ,  ]
            [1, 1, 0, 0, 1, 0]         ================>    [1, 1, 0, 0, 1, 0]      ========================>   [ ,  ,  ,  ,  ,  ]
            [1, 0, 1, 1, 0, 0]                              [1, 0, 0, 0, 0, 0]                                  [ ,  , 1, 1,  ,  ]
            [1, 0, 0, 0, 0, 1]                              [1, 0, 0, 0, 0, 1]                                  [ ,  ,  ,  ,  ,  ]


'''

black_white_img = [ [1, 0, 0, 0, 0, 0],
                    [0, 1, 0, 1, 1, 1],
                    [0, 0, 1, 0, 1, 0],
                    [1, 1, 0, 0, 1, 0],
                    [1, 0, 1, 1, 0, 0],
                    [1, 0, 0, 0, 0, 1] ]

row , column = len(black_white_img), len(black_white_img[0])
edges = []

for r in range(0, row):
    for c in range(0, column):
        if(r == 0 or r == row-1 or c == 0 or c == column -1):
            if(black_white_img[r][c] == 1):
                edges.append((r,c))
                black_white_img[r][c] = 2


def find_new_edges(img ,r, c, edges):
    try:
        left = img[r][c-1]
    except:
        left = 0

    try:
        right = img[r][c+1]
    except:
        right = 0

    try:
        top = img[r-1][c]
    except:
        top = 0
    
    try:
        bottom = img[r+1][c]
    except:
        bottom = 0

    if(left  == 1):
        edges.append((r, c-1))
        black_white_img[r][c-1] = 2
        find_new_edges(img, r, c-1, edges)

    if(right  == 1):
        edges.append((r, c+1))
        black_white_img[r][c+1] = 2
        find_new_edges(img, r, c+1, edges)

    if(top  == 1):
        edges.append((r-1, c))
        black_white_img[r-1][c] = 2
        find_new_edges(img, r-1, c, edges)
            
    if(bottom  == 1):
        edges.append((r+1, c))
        black_white_img[r+1][c] = 2
        find_new_edges(img, r+1, c, edges)
    
for i in range(len(edges)):
    r = edges[i][0]
    c = edges[i][1]
    find_new_edges(black_white_img, r, c, edges )


for r in range(row):
    for c in range(column):
        black_white_img[r][c] = 0


for i in range(len(edges)):
    r = edges[i][0]
    c = edges[i][1]
    black_white_img[r][c] = 1


for r in range(row):
    for c in range(column):
        print(black_white_img[r][c], end=", ")
    print()