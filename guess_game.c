#include <stdio.h>

int main() {
    int secret = 7; // You can make this random later
    int guess;

    printf("--- The Number Guessing Game ---\n");
    printf("I'm thinking of a number between 1 and 10.\n");

    while(1) {
        printf("Enter your guess: ");
        scanf("%d", &guess);

        if(guess == secret) {
            printf("Correct! You won. ✅\n");
            break;
        } else if(guess < secret) {
            printf("Too low! Try again. ⬆️\n");
        } else {
            printf("Too high! Try again. ⬇️\n");
        }
    }

    return 0;
}
