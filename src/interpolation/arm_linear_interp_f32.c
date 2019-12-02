/* ----------------------------------------------------------------------
* Copyright (C) 2010-2012 ARM Limited. All rights reserved.
*
* $Date:         17. January 2013
* $Revision:     V1.4.0
*
* Project:       CMSIS DSP Library
* Title:         arm_linear_interp_example_f32.c
*
* Description:   Example code demonstrating usage of sin function
*                and uses linear interpolation to get higher precision
*
* Target Processor: Cortex-M4/Cortex-M3
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions
* are met:
*   - Redistributions of source code must retain the above copyright
*     notice, this list of conditions and the following disclaimer.
*   - Redistributions in binary form must reproduce the above copyright
*     notice, this list of conditions and the following disclaimer in
*     the documentation and/or other materials provided with the
*     distribution.
*   - Neither the name of ARM LIMITED nor the names of its contributors
*     may be used to endorse or promote products derived from this
*     software without specific prior written permission.
*
* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
* "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
* LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
* FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
* COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
* INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
* BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
* LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
* CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
* LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
* ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
* POSSIBILITY OF SUCH DAMAGE.
 * -------------------------------------------------------------------- */

#include "arm_math.h"
#include "math_helper.h"
#include "sensorlink_arm_math.h"

/*------------------------------------------------------------------------------
*  External table used for linear interpolation
*------------------------------------------------------------------------------*/
/*
This set of functions implements Linear interpolation process for Q7, Q15, Q31,
 and floating-point data types. The functions operate on a single sample of data
  each call to the function returns a single processed value.
S points to an instance of the Linear Interpolate function data structure.
 x is the input sample value. The functions returns the output value.
 if x is outside of the table boundary, Linear interpolation returns 
 first value of the table 
 if x is below input range and returns last value of table if x is above range.
*/
#define XSPACING    0.00005f 


extern float arm_linear_interep_table[188495];


bool slm_linear_interpolation(void)
{
  uint32_t i,j;
  arm_status status;

  arm_linear_interp_instance_f32 S = {188495, -3.141592653589793, XSPACING, &arm_linear_interep_table[0]};
  for(i=0; i< ALG_BUFFER_W-1 ; i++){
    for(j = 0; j<ALG_INTERPOLATION;j++)  {
        Proc.interpolated_data[i] = arm_linear_interp_f32(&S, Proc.raw_data[i]);
        }
  }

  /*------------------------------------------------------------------------------
  *            SNR calculation for method 1
  *------------------------------------------------------------------------------*/
  snr1 = arm_snr_f32(testRefSinOutput32_f32, testOutput, 2);

  /*------------------------------------------------------------------------------
  *            SNR calculation for method 2
  *------------------------------------------------------------------------------*/
  snr2 = arm_snr_f32(testRefSinOutput32_f32, testLinIntOutput, 2);

  /*------------------------------------------------------------------------------
  *            Initialise status depending on SNR calculations
  *------------------------------------------------------------------------------*/
  if ( snr2 > snr1)
  {
    status = ARM_MATH_SUCCESS;
  }
  else
  {
    status = ARM_MATH_TEST_FAILURE;
  }

  /* ----------------------------------------------------------------------
  ** Loop here if the signals fail the PASS check.
  ** This denotes a test failure
  ** ------------------------------------------------------------------- */
  if ( status != ARM_MATH_SUCCESS)
  {
    while (1);
  }

  while (1);                             /* main function does not return */
}
