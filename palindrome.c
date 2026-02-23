#include<stdio.h>
#include<conio.h>

void main()
{
    int num,sum=0,rev=0,x,d;
    printf("Enter a number:");
    scanf("%d",&num);
    x=num;
    while(num>0)
    {
        d=num%10;
        sum=sum+d;
        num=num/10;
        rev=rev*10+d;
    
    }
    printf("Sum of digits is %d\n",sum);
    printf("Reverse of the number is %d\n",rev);
    if(x==rev)
    {
        printf("The number is palindrome");
    }
    else
    {
        printf("The number is not palindrome");
    }
    getch();
    
}