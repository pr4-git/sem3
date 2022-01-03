#include <stdio.h>

int main(int argc, char *argv[])
{
    for (int i = 0; i < argc; i++)
    {
        printf("argc is %d and argv is %s\n", i, argv[i]);
    }
}