#pragma once
#include "arm_math.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>


//LSB of ADC dumped 
#define ADC_BITS 15U
#define SAMP_RANGE (2**ADC_BITS)U
#define SAMP_MIN (-SAMP_RANGE/2)U
#define SAMP_MAX (SAMP_RANGE/2 -1)U


#define ALG_BUFFER_W    4096U
#define ALG_SAMP_RATE   60000000.0f
#define ALG_INTERPOLATION 10
#define ALG_TIME_RES    1/ALG_SAMP_RATE
#define ALG_SLIDING_SUBWIN 16
#define ALG_GUARD_SAMPLES 2

static struct {
    float raw_data[ALG_BUFFER_W];
    float sliding_win_leading[ALG_SLIDING_SUBWIN];
    float sliding_win_leading[ALG_SLIDING_SUBWIN];
    float cell_under_test;
    float interpolated_data[ALG_INTERPOLATION * ALG_BUFFER_W];
    bool input_data_valid;
    bool interpol_data_valid;
    bool proc_done;

}Proc;


extern void arm_biquad_cascade_df1_f32(const arm_biquad_casd_df1_inst_f32 * S, float32_t * pSrc, float32_t * pDst, uint32_t blockSize);
extern void arm_biquad_cascade_df1_init_f32( arm_biquad_casd_df1_inst_f32 * S, uint8_t numStages, float32_t * pCoeffs, float32_t * pState);
extern void arm_correlate_f32( float32_t * pSrcA, uint32_t srcALen, float32_t * pSrcB, uint32_t srcBLen, float32_t * pDst);




