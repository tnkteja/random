#include<stdio.h>
#include<iostream>
#include<malloc.h>

int function(const int one, char* const two,const char* three){
    /*
     *
     */
    
    return 0;
}

typedef struct _name{
    void* pointer;
} Name;

class BaseClass{
    
    protected:
      int prv1;
    
    public:
      int puv1;
       
      virtual BaseClass& method(){
          printf("If called from base ref or pointer or the base object or base ref or base pointer to derived object wothout verridden method");
      }
    
      int method2() final {
      }
      
      virtual ~BaseClass(){
          
      }
}


class AbstractBaseClass {
    /*
     * Cannot be instantiated should only deried and instantiated.
     */
    
    protected:
    int v1;
    
    public:
      // pure virtual function or abstract function
      virtual int method() = 0;
    
      virtual int method2() = 0 {
         printf("Pure virtual function with a default implementation");
      }
      
       virtual ~AbstractBaseClass(){
       }
}

class IinterfaceBaseClass {
    public:
    virtual int method1() = 0;
    virtual int method2() = 0;
    
    virtual ~Interfacebase(){
    }
}

// UNRESOLVED: derived from two classes with methods having same signature.

class DerivedClass: public BaseClass, virtual public AbstractBaseClass {

    public:
   // Covariant return tyes
   DerivedClass& method() override {
        printf("If called from a base Ref or base Pointer of a Derived object");
    }
   
    int AbstractbaseClass::method() final{
    }
    
    //using default implementation.
    int method2(){
        return AbstractBaseClass::method2();
    }
}

class DerivedClass2: virtual public BaseClass, virtual public AbstractBaseClass {
    
}

struct structName{
    private:
}

class GrandDerivedClass{
}

int main(unsigned int argc, char** argv){
    
    int r=function(0,0,'\0'); \\ Early binding
    int (fptr*)(const int, char* const, const char *) = function;
    fptr(0,0,'\0');  \\ late bnding
        
    int sA[10]={0,2,3};
    
    int sA2[10]{0,6,8};
 
    
    int* dynamicArray=(int*)malloc(10*sizeof(int));
    for(int i=0;i<10;i++){
        dynamicArray[i]=0;
    }
    
    int * dA2 = new int[10]{0,6,6};   
    
    // Deallocate or delete
    
    BaseClass base();
    DerivedClass derived(5);
    
    BaseClass& baseref= derived;
    
    BaseClass* baseptr=derived;
    
    baseref.method();
    baseref.BaseClass.method();
    
    BaseClass* baseArr=new BaseClass*[10]{ &derived, &base};
    \\ Unresolve the sizes of the derived cass would be different, and allocating ht earray would be disprportionalte.
   
}
