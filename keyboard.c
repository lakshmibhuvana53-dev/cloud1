#include<stdio.h>
#include<conio.h>

void main()
{
    int n,sum=0;
    printf("\n To stop entering input enter 999");
    do
    {
        printf("\n Enter the input number:");
        scanf("%d",&n);
        if(n>0 && n!=999)
        {
            sum=sum+n;
        }
    }    
        while(n!=999);   
        printf("\n The sum of positive input numbers are: %d",sum);
    
    
    getch();

}