#include <stdio.h>
int main () {
    float Base,Height,area;
    //input 
    printf("enter base of triangle: ");
    scanf ("%f", &Base);
    printf("enter height of triangle: ");
    scanf ("%f", &Height);
    //process
    area=0.5*(Base*Height);
    //output
    printf(" area of triangle :%0.2f", area);
}