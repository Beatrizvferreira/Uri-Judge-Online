/*
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>


int main(){

int A;
double B,total;

scanf("%d %lf",&A,&B);
total=A/B;
printf("%.3lf km/l\n",total);

return 0;
}
