#include <stdio.h>
int main () {
    float drink,food,item,sumdrink,sumfood,sumitem,total,cost,i;
    sumdrink=0;
    sumfood=0;
    sumitem=0;
    
    printf("Enter your cost : ");
    scanf("%f", &cost);
    
    while (1) {
        printf("drink : ");
        scanf ("%f", &drink);
        sumdrink = drink+sumdrink;
        if (drink==0) {
            break;
        }
        }
    while (1) {
        printf("food : ");
        scanf ("%f", &food);
        sumfood = food+sumfood;
        if (food==0) {
            break;
        }
        }
    while (1) {
        printf("item : ");
        scanf ("%f", &item);
        sumitem = item+sumitem;
        if (item==0) {
            break;
        }
        }
    i=sumdrink*0.20;
    i=i+(sumfood*0.50);
    i=i+(sumitem*0.10);
    total=sumdrink+sumfood+sumitem;
    printf("drink income today is : %.2f \n", sumdrink);
    printf("food income today is : %.2f \n", 
        sumfood);
    printf("item income today is : %.2f \n", 
        sumitem);
    printf("total to day is %.2f \n", total);
    printf("profit %.2f \n", i);
    printf("income %.2f", total-cost);
}