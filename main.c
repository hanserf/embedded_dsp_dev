#include "stdio.h"
#include "string.h"
#include "stdint.h"
#include "stddef.h"
#include "stdbool.h"


#define BUFFER_W    4096U
#define SAMP_RATE   60000000.0f
#define INTERPOLATION 10
#define TIME_RES    1/SAMP_RATE
#define XSPACING    TIME_RES/INTERPOLATION 

/** Math functions for IIR filtering and interpolation.
 * Looks at a raw signal
 * Does IIR filtering for fundamental frequency.
 * Interpolates the signal using linear interpolation with a LUT
 * of sine values baseed on CMSIS Example.
 * Identify noise floor of signal.
 * Identify peaks
 * Calculate SNR for echoes
 * 
 * 
 * */

static int16_t get_max_value(int16_t *buffer, uint16_t size){
    uint16_t i ;
    int16_t tmp_max = 0;
    for(i = 0; i < size ; i++){
        if(buffer[i]>tmp_max){
            tmp_max = buffer[i];
        }
    }
    return tmp_max;
}

static int16_t get_min_value(int16_t *buffer, uint16_t size){
    uint16_t i ;
    int16_t tmp_min = 0;
    for(i = 0; i < size ; i++){
        if(buffer[i]<tmp_min){
            tmp_min = buffer[i];
        }
    }
    return tmp_min;
}


bool int_to_float_normalize(int16_t *buf,uint16_t buf_w){
    int16_t max_val, min_val, diff;
    uint16_t i;
    float max_f,min_f;
    bool success = false;
    max_f = 0;
    if(buf_w <= BUFFERSIZE){
        max_val = get_max_value(buf,buf_w);
        min_val = get_min_value(buf,buf_w);
        diff = max_val + min_val;
        if(diff>=0){
            max_f = (float)max_val;
        }
        else
        {
            max_f = -(float)min_val;
        }
        for(i = 0; i < buf_w; i++){
            Proc.raw_data[i] = (float)buf[i]/max_f;
        }
        success = true;
        Proc.input_data_valid = true;
    }
    return success;
}







void spline_interpolation() {
    /** Step 0 */
    int n, i, j;
    scanf("%d", &n);
    n--;
    float x[n + 1], a[n + 1], h[n], A[n], l[n + 1],
        u[n + 1], z[n + 1], c[n + 1], b[n], d[n];
    for (i = 0; i < n + 1; ++i) scanf("%f", &x[i]);
    for (i = 0; i < n + 1; ++i) scanf("%f", &a[i]);

    /** Step 1 */
    for (i = 0; i <= n - 1; ++i) h[i] = x[i + 1] - x[i];

    /** Step 2 */
    for (i = 1; i <= n - 1; ++i)
        A[i] = 3 * (a[i + 1] - a[i]) / h[i] - 3 * (a[i] - a[i - 1]) / h[i - 1];

    /** Step 3 */
    l[0] = 1;
    u[0] = 0;
    z[0] = 0;

    /** Step 4 */
    for (i = 1; i <= n - 1; ++i) {
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * u[i - 1];
        u[i] = h[i] / l[i];
        z[i] = (A[i] - h[i - 1] * z[i - 1]) / l[i];
    }

    /** Step 5 */
    l[n] = 1;
    z[n] = 0;
    c[n] = 0;

    /** Step 6 */
    for (j = n - 1; j >= 0; --j) {
        c[j] = z[j] - u[j] * c[j + 1];
        b[j] = (a[j + 1] - a[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3;
        d[j] = (c[j + 1] - c[j]) / (3 * h[j]);
    }

    /** Step 7 */
    printf("%2s %8s %8s %8s %8s\n", "i", "ai", "bi", "ci", "di");
    for (i = 0; i < n; ++i)
        printf("%2d %8.2f %8.2f %8.2f %8.2f\n", i, a[i], b[i], c[i], d[i]);
    return 0;
}

int main(){




    return 0;
}