#include <stdio.h>
#include <conio.h>

void main()
{
    int vote;
    printf("Enter your age: ");
    scanf("%d", &vote);

    if (vote>18)
    {
        printf("Your eligible for vote");
    }
    else
    {
        printf("You are not eligible for vote");

    }
    getch();
    
}
