#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>

int main(int argc, char *argv[])
{

    printf("The PID of ex1 is %d\n", getpid());
    char *args[]={"./ex2", NULL};
    execv(args[0],args);
    printf("Back to ex1\n");
    return 0;
}


