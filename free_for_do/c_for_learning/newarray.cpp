#include<stdio.h>
int main (){ //    int a[100][100][100],sum[100],sumr[100][100];int i,n,u,o,p,r;
    int a[100][100][100],sum[100],sumr[100][100];
    int i,n,u,o,p,r;
    i=0,u=0,p=5,o=0,r=0;
    printf("input amount of studen : ");
    scanf("%d", &n);
    printf("\nyou need to input score for %d student \n", n);
    printf("first term score\n");
    for (r=0;r<2;r++){
        for (u=0,o=0;u<n;u++,o++){
            sumr[r][u]=sum[u];
            
            for (i=0;i<p;i++){
                printf("input student %d score : ", u+1);
                scanf("%d", &a[r][o][i]);
                sum[u]+=a[r][o][i]; 
                             }   }
        for (i=0,o=0;i<n;i++,o++){
            printf("\nin first term[%d]", sumr[r][i]);
            printf("student%d :", i+1);
            for (u=0;u<p;u++)
                printf("%d:", a[r][o][u]);}
                        if (r<1)
                            printf("\nlast term score\n");}
    for (u=0;u<n;u++){
    printf("\ntotal studen%d score : %d the grade is :", u+1, sum[u]);
    if (sum[u] >= 80) 
        printf(" A\n");
    if (sum[u] >= 70 && sum[u] < 80) 
        printf(" B\n");
    if (sum[u] >= 60 && sum[u] < 70)
        printf(" C\n");
    if (sum[u] >= 50 && sum[u] < 60) 
        printf(" D\n");
    if (sum[u] < 50) 
        printf(" F\n");}
    }