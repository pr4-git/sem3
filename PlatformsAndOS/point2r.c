#include <stdio.h>

void swap(int *x, int *y) // takes addresses
{
    // swapping values in the addresses
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

int main(void)
{
    int a, b;
    printf("Enter the value of a and b: \n");
    scanf("%d %d", &a, &b);
    printf("The value from the user input for a is %d and for b is %d", a, b);
    // sending address to function
    swap(&a, &b);
    printf("\nThe swapped value of a is %d and b is %d", a, b);
}