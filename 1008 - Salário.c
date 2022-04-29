#include <stdio.h>

int main() {

   int number, horas;
   float valor, salary;

   scanf("%d",&number);
   scanf("%d",&horas);
   scanf("%f",&valor);

   salary = horas*(float)valor;

   printf("NUMBER = %d\n",number);
   printf("SALARY = U$ %.2f\n",salary);


    return 0;
}
