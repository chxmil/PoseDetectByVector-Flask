#include <stdio.h>
typedef struct std st;
struct std{
    char name[30];
    char flight[30];
    char seat[30];
    
};
int main() {
    st std[100];
    int n,i;
    printf("enter your amount passenger:");
    scanf("%d", &n);
    for(i=0;i<n;i++){
        printf("\npassenger name:");
        scanf("%s", std[i].name);
        printf("\nflight name:");
        scanf("%s", std[i].flight);
        printf("\npassenger seat:");
        scanf("%s", std[i].seat);
    }
    for(i=0;i<n;i++){
    printf("\npassenger%d", i+1);
    printf("\nname:%s\nflight:%s\n", std[i].name, std[i].flight);
    printf("seat:%s \n", std[i].seat);

    }
    return 0;
}