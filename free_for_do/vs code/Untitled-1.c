#include <stdio.h>
int main() {
    float weight,high,bmi;
    
    printf("please enter your weight ");
    scanf("%f",&weight);
    
    printf("please enter your high ");
    scanf("%f",&high);
    
    high=high*0.01;
    high=high*high;
    bmi = weight/high;
    
    if (bmi<18.5)
        printf("you are skinny");
    else
        if (bmi<22.90)
            printf("you are normal");
    else
        if (bmi<24.90)
            printf("you are chubby");
    else
        if (bmi>24.90)
            printf("you are fat");
            
printf("\nyour bmi is %.2f", bmi);
    
    
}