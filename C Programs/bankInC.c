#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LENGTH 50

struct Customer {
    char name[MAX_NAME_LENGTH];
    double balance;
};

void deposit(struct Customer *customer, double amount) {
    customer->balance += amount;
    printf("After deposit, balance is: %.2f\n", customer->balance);
}

void withdraw(struct Customer *customer, double amount) {
    if (amount > customer->balance) {
        printf("Insufficient fund, can't perform the operation...!!\n");
    } else {
        customer->balance -= amount;
        printf("After withdraw, balance is: %.2f\n", customer->balance);
    }
}

void knowBalance(struct Customer *customer) {
    printf("Your current balance is: %.2f\n", customer->balance);
}

int main() {
    FILE *file = fopen("bankdata.txt", "r+");
    if (file == NULL) {
        printf("Error opening file. Exiting...\n");
        return 1;
    }

    struct Customer customer;
    printf("Enter your name: ");
    fgets(customer.name, sizeof(customer.name), stdin);
    customer.name[strcspn(customer.name, "\n")] = '\0';

    printf("Hello %s ❤️\n", customer.name);

    while (1) {
        printf("d - deposit some amount\n");
        printf("w - withdraw some amount\n");
        printf("b - know your balance\n");
        printf("e - exit\n");
        printf("Choose your option: ");

        char option;
        scanf(" %c", &option);

        switch (option) {
            case 'd': {
                double amount;
                printf("Enter your amount: ");
                scanf("%lf", &amount);
                deposit(&customer, amount);
                break;
            }
            case 'w': {
                double amount;
                printf("Enter your amount: ");
                scanf("%lf", &amount);
                withdraw(&customer, amount);
                break;
            }
            case 'b':
                knowBalance(&customer);
                break;
            case 'e':
                printf("Thanks for banking...!!\n");
                break;
            default:
                printf("You've chosen a wrong option, please choose an option from the given list\n");
                break;
        }

        // Move file pointer to the beginning to update the customer's balance
        fseek(file, 0, SEEK_SET);
        fwrite(&customer, sizeof(struct Customer), 1, file);
        if(option == 'e'){
            break;
        }
    }

    fclose(file);
    return 0;
}
