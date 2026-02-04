#include <stdio.h>
#include <conio.h>

void main()
{
    char c ;
    printf("Enter a character: ");
    c = getchar();
    if (c == 'y' || c == 'Y')
    {
        printf("Agreed.\n");
    }
    else if (c == 'n' || c == 'N')
    {
        printf("Not agreed.\n");
    }
    else
    {
        printf("Invalid input.\n");
    }
    getch();

}