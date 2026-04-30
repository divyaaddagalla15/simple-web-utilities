#include <stdio.h>

int main() {
    char tasks[3][50];
    printf("--- My Daily Tasks ---\n");

    for(int i = 0; i < 3; i++) {
        printf("Enter task %d: ", i + 1);
        scanf("%s", tasks[i]);
    }

    printf("\nYour List for Today:\n");
    for(int i = 0; i < 3; i++) {
        printf("%d. %s\n", i + 1, tasks[i]);
    }

    return 0;
}
