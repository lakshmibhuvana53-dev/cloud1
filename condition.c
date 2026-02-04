#include<stdio.h>
#include<conio.h>

int main()
{
    int num;
    printf("Enter an integer: ");
    scanf("%d", &num);

    if (num > 0)
    {
        printf("The number is a positive integer. \n");
    }
    else if (num < 0)
    {
        printf("The number is a negative integer. \n");
    }
    else
    {
        printf("The number is zero. \n");
    }
    getch();
    return 0;

}
