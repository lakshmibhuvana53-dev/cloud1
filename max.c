#include<stdio.h>
#include<conio.h>

void main()
{
        int a,b,c,max;
        printf("Enter the values of 3 integers: ");
        scanf("%d %d %d",&a,&b,&c);
        if(a>b)
        {
                max=a;
            
        if(a>c)
            {
                max=a;
            }    
        else
            {
                max=c;
            }
        }
        else
            {
                if(b>c)
                    {
                        max=b;
                    }
            
                else
                {
                    max=c;
                }
            }
        printf("\n The Biggest of 3 numbers is:%d",max);
        getch();         

}