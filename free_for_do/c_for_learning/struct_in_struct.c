#include <stdio.h>
typedef struct employee st;
struct employee{
    char name[30];
    char id[30];
    struct contact {
        char email[50];
        char phonenumber[50];
    }contact;

};
int main(){
    st employee,contact;
    printf("input name:");
    scanf("%s", employee.name);
    printf("\n input id:");
    scanf("%s", employee.id);
    printf("\n input email:");
    scanf("%s", employee.contact.email);
    printf("\n input phonenumber:");
    scanf("%s", employee.contact.phonenumber);
    
    printf(" name:");
    printf("%s", employee.name);
    printf("\n id:");
    printf("%s", employee.id);
    printf("\n email:");
    printf("%s", employee.contact.email);
    printf("\n phonenumber:");
    printf("%s", employee.contact.phonenumber);
}