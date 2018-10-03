ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP1()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_1 = -(MDL_EE*MDL_COMPLEXI)/3.000000D+00
      GC_2 = (2.000000D+00*MDL_EE*MDL_COMPLEXI)/3.000000D+00
      GC_3 = -(MDL_EE*MDL_COMPLEXI)
      GC_4 = MDL_EE*MDL_COMPLEXI
      GC_20 = -(MDL_CPWWWL2*MDL_EE*MDL_COMPLEXI)/(4.000000D+00
     $ *MDL_MW__EXP__2)
      GC_21 = (3.000000D+00*MDL_CWWWL2*MDL_EE*MDL_COMPLEXI)/(2.000000D
     $ +00*MDL_MW__EXP__2)
      GC_47 = (MDL_EE*MDL_COMPLEXI)/(MDL_SW*MDL_SQRT__2)
      GC_48 = (MDL_CKM1X1*MDL_EE*MDL_COMPLEXI)/(MDL_SW*MDL_SQRT__2)
      GC_49 = (MDL_CKM1X2*MDL_EE*MDL_COMPLEXI)/(MDL_SW*MDL_SQRT__2)
      GC_50 = (MDL_CKM2X1*MDL_EE*MDL_COMPLEXI)/(MDL_SW*MDL_SQRT__2)
      GC_51 = (MDL_CKM2X2*MDL_EE*MDL_COMPLEXI)/(MDL_SW*MDL_SQRT__2)
      GC_99 = (MDL_EE*MDL_COMPLEXI*MDL_CONJG__CKM1X1)/(MDL_SW
     $ *MDL_SQRT__2)
      GC_100 = (MDL_EE*MDL_COMPLEXI*MDL_CONJG__CKM1X2)/(MDL_SW
     $ *MDL_SQRT__2)
      GC_101 = (MDL_EE*MDL_COMPLEXI*MDL_CONJG__CKM2X1)/(MDL_SW
     $ *MDL_SQRT__2)
      GC_102 = (MDL_EE*MDL_COMPLEXI*MDL_CONJG__CKM2X2)/(MDL_SW
     $ *MDL_SQRT__2)
      END
