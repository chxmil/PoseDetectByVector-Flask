#include <stdio.h>
int main () {
    float Radius,Height,volume ;
    //input 
    printf("enter Radius of Cylindrical : ");
    scanf ("%f", &Radius);
    printf("enter height of Cylindrical : ");
    scanf ("%f", &Height);
    //process
    volume=3.141 * Radius * Radius * Height;
    //output
    printf(" volume of Cylindrical :%0.2f", volume);
}