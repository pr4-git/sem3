#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

void main(void)
{
    fork();
    printf("Hello world!\n");
}