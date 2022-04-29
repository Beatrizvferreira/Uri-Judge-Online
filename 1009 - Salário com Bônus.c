/*
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas
por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas
efetuadas, informar o total a receber no final do mês, com duas casas decimais.
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

typedef struct{

char nome[20];
double salario,vendas;

}TBox;

int main(){

TBox box;
double total;
scanf("%s %lf %lf",&box.nome,&box.salario,&box.vendas);
total=0.15*box.vendas+box.salario;

printf("TOTAL = R$ %.2lf\n",total);

return 0;
}
