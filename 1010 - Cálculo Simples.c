#include<stdio.h>
#include<stdlib.h>
#include<math.h>

typedef struct{

int codigo,qt;
float valor;

}TBox;

int main(){

int i=2;
TBox box[i];
float total;

scanf("%d %d %f",&box[1].codigo,&box[1].qt,&box[1].valor);
scanf("%d %d %f",&box[2].codigo,&box[2].qt,&box[2].valor);

total=box[1].qt*box[1].valor+box[2].qt*box[2].valor;

printf("VALOR A PAGAR: R$ %.2f\n",total);

return 0;
}