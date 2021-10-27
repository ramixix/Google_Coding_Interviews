# Task 1 "RemoveIslands" :
Imagine that you have an black and white image. As you know every image is constructed from small parts called pixel. Let's think that every pixel in our image is either black or white and let's say that number 1 represent pixels that are black and 0 represend pixels that are white. (think image as 2 dimensional array) for example our image might be like :
 
            [1, 0, 0, 0, 0, 0]
            [0, 1, 0, 1, 1, 1]
            [0, 0, 1, 0, 1, 0]
            [1, 1, 0, 0, 1, 0]
            [1, 0, 1, 1, 0, 0]
            [1, 0, 0, 0, 0, 1]
        
        Now Your task is to remove all black pixels that are not connected to the border ( note: if a black pixels be vertically or horizontally 
        conneted to other black pixels that are connected to borther, that black pixel should not get removed)
        for better Understanding take a look at example below :
        
            [1, 0, 0, 0, 0, 0]                              [1, 0, 0, 0, 0, 0]                                        [ ,  ,  ,  ,  ,  ]
            [0, 1, 0, 1, 1, 1]                              [0, 0, 0, 1, 1, 1]                                        [ , 1,  ,  ,  ,  ]
            [0, 0, 1, 0, 1, 0]         after operation      [0, 0, 0, 0, 1, 0]   the black pixels that get removed    [ ,  , 1,  ,  ,  ]
            [1, 1, 0, 0, 1, 0]         ================>    [1, 1, 0, 0, 1, 0]   =================================>   [ ,  ,  ,  ,  ,  ]
            [1, 0, 1, 1, 0, 0]                              [1, 0, 0, 0, 0, 0]                                        [ ,  , 1, 1,  ,  ]
            [1, 0, 0, 0, 0, 1]                              [1, 0, 0, 0, 0, 1]                                        [ ,  ,  ,  ,  ,  ]
