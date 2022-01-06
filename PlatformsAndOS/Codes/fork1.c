#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main(){

    int pid;
    pid = fork();

    if (pid==0)
        printf("Hello world from child! and the process id assigned by sys is %d and pid value is %d\n",getpid(),pid);

    else
        printf("Hello world from parent! and the process id is %d\n and pid value is %d\n",getpid(),pid);

    return 0;

}
