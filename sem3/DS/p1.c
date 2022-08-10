// function declration
#include<stdio.h>

int max(int a, int b);
int min(int a, int b);

int main()
{
    int a, b, maximum, minimum;

    printf("enter a: ");
    scanf("%d", &a);

    printf("enter b: ");
    scanf("%d", &b);

    maximum = max(a, b);
    minimum = min(a, b);

    printf("\nmaximum = %d", maximum);
    printf("\nminimum = %d", minimum);

return 0;
}

int max(int a, int b)
{
    return (a > b) ? a : b;
}
int min(int a, int b)
{
    return (b > a) ? a : b;
}