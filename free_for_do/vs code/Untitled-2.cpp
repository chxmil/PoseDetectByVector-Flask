#include <stdio.h>
int main() {
    int rate,oil,a,b,c,i;
    a=100;
    b=250;
    c=500;
    
    printf("please enter your oil consumption rate :");
    scanf("%d", &rate);
    
    printf("please enter your Fuel tank capacity :");
    scanf("%d", &oil);
    
    i=rate*oil;
    
    if (i<100)
        printf("รถคันนี้วิ่งได้ถึงเมือง A ");
    else
        if (i<250)
        printf("รถคันนี้วิ่งได้ถึงเมือง A,B ");
    else
        if (i<500)
        printf("รถคันนี้วิ่งได้ถึงเมือง A,B,C ");
    else
        if (i>=500)
        printf("รถคันนี้วิ่งได้ถึงเมือง A,B,C,D");
}