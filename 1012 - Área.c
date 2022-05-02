/*
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define pi 3.14159

typedef struct{

double Area;

}TArea;

int main(){

int i=5;
double A,B,C;
TArea box[i];

scanf("%lf %lf %lf",&A,&B,&C);

box[1].Area=(A*C)/2;     ///triângulo
box[2].Area=pi*pow(C,2); ///Circulo
box[3].Area=((A+B)*C)/2; ///Trapézio
box[4].Area=pow(B,2);    ///Quadrado
box[5].Area=A*B;         ///Retângulo

printf("TRIANGULO: %.3lf\n",box[1].Area);
printf("CIRCULO: %.3lf\n",box[2].Area);
printf("TRAPEZIO: %.3lf\n",box[3].Area);
printf("QUADRADO: %.3lf\n",box[4].Area);
printf("RETANGULO: %.3lf\n",box[5].Area);

return 0;
}
