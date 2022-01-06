#include<stdio.h>

int main(int argc, char *argv[])
{
    int i;
    for(int i=0; i<argc; i++)
    printf("argc: %d  argv: %s\n",i, argv[i]);
}


