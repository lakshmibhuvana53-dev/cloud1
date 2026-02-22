#include<stdio.h>
#include<conio.h>
#define PI 3.14159

void main()
{
        float r,area,circumference;
        printf("Enter the radius of circle : ");
        scanf("%f",&r);
        area=PI*r*r;
        circumference=2*PI*r;
        printf(" \n The area of circle is : %f",area);
        printf(" \n The circumference of circle is : %f",circumference);
        getch();

}