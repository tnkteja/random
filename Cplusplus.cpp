#include<stdio.h>
#include<iostream>
#include<malloc.h>

int globalFunction(const int one, char* const two,const char* three){
    /*
     *
     */
    
    return 0;
}

typedef struct _name{
    void* pointer;
} Name;

class className{
    public:   
}

struct structName{
    private:
}

int main(unsigned int argc, char** argv){
    
    int sA[10]={0,2,3};
    
    int sA2[10]{0,6,8};
 
    
    int* dynamicArray=(int*)malloc(10*sizeof(int));
    for(int i=0;i<10;i++){
        dynamicArray[i]=0;
    }
    
    int * dA2 = new int[10]{0,6,6};
    
    
    
    // Deallocate or delete
    
}
