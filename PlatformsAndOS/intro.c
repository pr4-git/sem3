#include <stdio.h>

int main(void)
{
    int *p;
    int a = 10;
    p = &a;
    printf("The value of a is %d", *&a);
    printf("\nThe value of p is %p", p);
    printf("\nThe value stored in the address pointed by p is %d", *p);
}