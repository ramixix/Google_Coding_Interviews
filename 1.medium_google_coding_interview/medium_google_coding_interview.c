#include <stdio.h>
#include <stdlib.h>

#define ROW 6
#define COLUMN 6



void check_node(int pixels[][COLUMN], int row, int column){
    if(pixels[row][column] == 1){
        pixels[row][column] =2;
     
        if( !(row-1 < 0) ){
            check_node(pixels, row-1, column);
        }
        if(row+1 != ROW){
            check_node(pixels, row+1, column);
        }
        if(!(column-1 < 0)){
            check_node(pixels, row, column-1);
        }
        if(column+1 != COLUMN){
            check_node(pixels, row, column+1);
        }
    }
}

int main(int argc, char *argv[]){
 

    int pixels[ROW][COLUMN]= {  {1, 0, 0, 0, 0, 0},
                                {0, 1, 0, 1, 1, 1},
                                {0, 0, 1, 0, 1, 0},
                                {1, 1, 0, 0, 1, 0},
                                {1, 0, 1, 1, 0, 0},
                                {1, 0, 0, 0, 0, 1} };
                                

    for (int r = 0; r < ROW; r++){
        for (int c = 0; c < COLUMN; c++){
            if(r==0 || r==ROW-1 || c==0 || c==COLUMN-1)
                check_node(pixels, r, c);
        }
    }

    for (int r = 0; r < ROW; r++){
        for (int c = 0; c < COLUMN; c++){
            if(pixels[r][c] == 1){
                pixels[r][c] =0;
            }
            if(pixels[r][c] == 2){
                pixels[r][c] = 1;
            }
            printf("%d ", pixels[r][c]);
        }
        printf("\n");
    }

}