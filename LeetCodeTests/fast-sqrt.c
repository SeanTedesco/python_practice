#include "stdio.h"
#include "math.h"
#include "time.h"

float q_sqrt( float number )
{
    long i;
    float x2, y;
    const float threehalfs = 1.5F;

    x2 = number * 0.5F;
    y = number;
    i = * ( long* ) &y;
    i = 0x5f3759df - ( i >> 1 );
    y = * ( float* ) &i;
    y = y * ( threehalfs - (x2 * y * y) );

    return y;
}

int main()
{
    float val = 1.2; 

    clock_t begin = clock();
    float slow_val = 1 / sqrt(val);
    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Value: %f in %1.9f seconds\n", slow_val, time_spent);

    clock_t begin1 = clock();
    float fast_val = q_sqrt(val);
    clock_t end1 = clock();
    double time_spent1 = (double)(end1 - begin1) / CLOCKS_PER_SEC;
    printf("Value: %f in %1.9f seconds\n", fast_val, time_spent1);
    
    return 0; 
}