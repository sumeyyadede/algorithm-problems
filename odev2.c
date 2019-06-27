#include <stdio.h>
#include <math.h>
#define TOL 0.001

float func(float x){
    return (x*x - 2*x - 2);
}

int main()
{
    int i = 1, No = 10;
    float Po = 1.5;
    double p;

    while(i <= No){
        p = func(Po);
        if(fabs(p - Po) <= TOL){
            break;
        }
        printf("\nIterasyon: %d Simdiki deger: %lf", i, p);
        i = i + 1;
        Po = p;
    }

    printf("\np degeri = %lf\n", p);
    return 0;     
}
