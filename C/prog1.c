#include<stdio.h>
void fun(){
    static int x = 0;
    x++;
    printf("%d ",x);
    x=x+1;
    printf("%d\n",x);
}
int main(){
    fun();
    fun();
    fun();

}