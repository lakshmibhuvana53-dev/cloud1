#include<stdio.h>
#include<conio.h>
void main()
{
    int per;
    printf("Enter your percentage: ");
    scanf("%d",per);

    if(per<0)
    {
        printf("\n Percentage cannot be negative.");
    }
    else if (per<=35)
    {
        printf("\n You have failed.");
    }
    else if(per<50)
    {
        printf("\n You have passed with Third class.");
    }
    else if(per<70)
    {
        printf("\n You have passed with Second class.");
    }
    else if(per<85)

    {
        printf("\n You have passed with First class.");
    }
    else if(per<=100)
    {
        printf("\n you have passed with First class distinction.Congratulations!");
    
}
    else
    {
        printf("\n Percentage cannot be greater than 100.");
    }
    getch();
}