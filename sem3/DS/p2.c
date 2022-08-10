// call by reference

#include <stdio.h>

void swap(int*, int*);  //pointer (*)

int main()
{
    int a = 10, b = 20;

    swap(&a, &b);   //passes reference like(a -> b and b -> a)
    
    printf("\na = %d\nb = %d", a, b);

    return 0;
}

void swap(int* x, int* y)     //pointer to an integer  (*x or *y)
{
    int t;

    t = *x;
    *x = *y;
    *y = t;

    printf("\nx = %d\ny = %d", *x, *y);
}


/* putting "\n" before every variable because every variable/pointer 
contains int */
