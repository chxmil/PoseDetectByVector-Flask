#include <stdio.h>
int main() {
    int numb;
    printf("please enter number 1-100 : ");
    scanf("%d", &numb);
    if (numb >= 1 && numb <= 100)
    {
    if (numb % 7 == 0)
    printf("buzz-buzz");
    
    if (numb % 10 == 7)
    printf("buzz");
    
    if (numb % 10 != 7 && numb % 7 != 0)
         printf("%d", numb);
        
    }
    else
        printf("your enter number is not 1-100");
}