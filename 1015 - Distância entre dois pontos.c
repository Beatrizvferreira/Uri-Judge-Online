/*
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano,
p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distância= sqrt(pow(x1-y1,2)+pow(x2-y2,2))
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){

double x1,x2,y1,y2;
double aux,aux2,distancia;

scanf("%lf %lf",&x1,&y1);
scanf("%lf %lf",&x2,&y2);

aux=x2-x1;
aux2=y2-y1;
distancia=sqrt(pow(aux,2)+pow(aux2,2));
printf("%.4lf\n",distancia);

return 0;
}
