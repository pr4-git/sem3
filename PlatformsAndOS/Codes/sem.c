#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>
#include<pthread.h>
#include<semaphore.h>

#define THREAD_NUM 4

sem_t semaphore;

void* routine(void* args)
{

}

int main(int argc, char* argv[])
{
    pthread_t th[THREAD_NUM];
    sem_init(&semaphore, 0, 1);
    int i;
    for(i=0; i < THREAD_NUM; i++){
        if(pthread_create(&th[i], NULL, &routine, NULL) != 0){
            perror("Failed to create thread");
        }
    }

    for (i=0; i< THREAD_NUM; i++){
      if (pthread_join(th[i],NULL) != 0){
        perror("Failed to join thread");
      }
    }
    sem_destroy(&semaphore);
    return 0;
}
