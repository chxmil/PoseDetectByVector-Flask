#include <stdio.h>

int main () {
    //โจทย์ใน line
    int num[100], position[100], allnum[100], num2[100];
    int temp, input, length, test;
    int i, j, k, e=0;

    //input
    for (length=0 ; length<100 ; length++) {
        scanf("%d", &input);
        if (input<=0) {
            break;
        }
        num[length] = input;
        num2[length] = input;
    }

    //เรียงใหม่
    for (i=0 ; i<length ; i++){
        for (j=1 ; j<length ; j++){
            if (i<j && num2[i]>num2[j]) {
                temp = num2[i];
                num2[i] = num2[j];
                num2[j] = temp;
            }
        }
    }

    //ย่ออันที่เรียง
    for (i=0 ; i<length ; i++){
        test=num2[i];
        k=0;
        for (j=0 ; j<i ; j++) {
            if (test==num2[j]){
                k=1;
                break;
            }
        }
        if (k==0) {
            allnum[e]=test;
            e++;
        }
    }

    //output
    for (i=0; i<e ; i++){
        printf("%d occurs ", allnum[i]);
        k=0;
        for (j=0 ; j<length ; j++){
            if (allnum[i] == num[j]){
                position[k] = j+1;
                k++;
            }
        }
        printf("%d times at position ", k);
        for (j=0 ; j<k ; j++){
            if (j==(k-1))
                printf("%d\n", position[j]);
            else
                printf("%d, ", position[j]);
        }
    }

    return 0;
}