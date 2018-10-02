# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.1.1 for Mac OS X x86 (64-bit) (April 18, 2017)
# Date: Sun 23 Sep 2018 15:47:53


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


UUS1 = Lorentz(name = 'UUS1',
               spins = [ -1, -1, 1 ],
               structure = '1')

UUV1 = Lorentz(name = 'UUV1',
               spins = [ -1, -1, 3 ],
               structure = 'P(3,2) + P(3,3)')

SSS1 = Lorentz(name = 'SSS1',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS1 = Lorentz(name = 'FFS1',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1)')

FFS2 = Lorentz(name = 'FFS2',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) - ProjP(2,1)')

FFS3 = Lorentz(name = 'FFS3',
               spins = [ 2, 2, 1 ],
               structure = 'ProjP(2,1)')

FFS4 = Lorentz(name = 'FFS4',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) + ProjP(2,1)')

FFV1 = Lorentz(name = 'FFV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV2 = Lorentz(name = 'FFV2',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV3 = Lorentz(name = 'FFV3',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

VSS1 = Lorentz(name = 'VSS1',
               spins = [ 3, 1, 1 ],
               structure = 'P(1,2) - P(1,3)')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVV1 = Lorentz(name = 'VVV1',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVV2 = Lorentz(name = 'VVV2',
               spins = [ 3, 3, 3 ],
               structure = '-(P(1,2)*P(2,3)*P(3,1)) + P(1,3)*P(2,1)*P(3,2) + P(-1,2)*P(-1,3)*P(3,1)*Metric(1,2) - P(-1,1)*P(-1,3)*P(3,2)*Metric(1,2) - P(-1,2)*P(-1,3)*P(2,1)*Metric(1,3) + P(-1,1)*P(-1,2)*P(2,3)*Metric(1,3) + P(-1,1)*P(-1,3)*P(1,2)*Metric(2,3) - P(-1,1)*P(-1,2)*P(1,3)*Metric(2,3)')

VVV3 = Lorentz(name = 'VVV3',
               spins = [ 3, 3, 3 ],
               structure = '-2*Epsilon(1,2,3,-2)*P(-2,3)*P(-1,1)*P(-1,2) - 2*Epsilon(1,2,3,-2)*P(-2,2)*P(-1,1)*P(-1,3) - 2*Epsilon(1,2,3,-2)*P(-2,1)*P(-1,2)*P(-1,3) + Epsilon(2,3,-1,-2)*P(-2,3)*P(-1,1)*P(1,2) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*P(1,2) + Epsilon(2,3,-1,-2)*P(-2,2)*P(-1,1)*P(1,3) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,2)*P(1,3) - Epsilon(1,3,-1,-2)*P(-2,3)*P(-1,2)*P(2,1) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,3)*P(2,1) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,1)*P(2,3) - Epsilon(1,3,-1,-2)*P(-2,1)*P(-1,2)*P(2,3) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2)*P(3,1) + Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,3)*P(3,1) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*P(3,2) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,3)*P(3,2) - (Epsilon(3,-1,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*Metric(1,2))/2. + (Epsilon(3,-1,-2,-3)*P(-3,3)*P(-2,1)*P(-1,2)*Metric(1,2))/2. - (Epsilon(3,-1,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*Metric(1,2))/2. + (Epsilon(3,-1,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*Metric(1,2))/2. + (Epsilon(2,-1,-2,-3)*P(-3,2)*P(-2,3)*P(-1,1)*Metric(1,3))/2. + (Epsilon(2,-1,-2,-3)*P(-3,3)*P(-2,1)*P(-1,2)*Metric(1,3))/2. - (Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,3)*P(-1,2)*Metric(1,3))/2. - (Epsilon(2,-1,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*Metric(1,3))/2. - (Epsilon(1,-1,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*Metric(2,3))/2. + (Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,3)*P(-1,1)*Metric(2,3))/2. - (Epsilon(1,-1,-2,-3)*P(-3,1)*P(-2,3)*P(-1,2)*Metric(2,3))/2. + (Epsilon(1,-1,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*Metric(2,3))/2.')

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV2 = Lorentz(name = 'VVVV2',
                spins = [ 3, 3, 3, 3 ],
                structure = '-(Epsilon(1,2,3,4)*P(-1,1)*P(-1,3)) + Epsilon(1,2,3,4)*P(-1,2)*P(-1,3) + Epsilon(1,2,3,4)*P(-1,1)*P(-1,4) - Epsilon(1,2,3,4)*P(-1,2)*P(-1,4) - Epsilon(2,3,4,-1)*P(-1,3)*P(1,2) + Epsilon(2,3,4,-1)*P(-1,4)*P(1,2) - Epsilon(2,3,4,-1)*P(-1,1)*P(1,3) - Epsilon(2,3,4,-1)*P(-1,2)*P(1,3) + Epsilon(2,3,4,-1)*P(-1,1)*P(1,4) + Epsilon(2,3,4,-1)*P(-1,2)*P(1,4) - Epsilon(1,3,4,-1)*P(-1,3)*P(2,1) + Epsilon(1,3,4,-1)*P(-1,4)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,1)*P(2,3) - Epsilon(1,3,4,-1)*P(-1,2)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,1)*P(2,4) + Epsilon(1,3,4,-1)*P(-1,2)*P(2,4) - Epsilon(1,2,4,-1)*P(-1,3)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,4)*P(3,1) + Epsilon(1,2,4,-1)*P(-1,3)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,4)*P(3,2) - Epsilon(1,2,4,-1)*P(-1,1)*P(3,4) + Epsilon(1,2,4,-1)*P(-1,2)*P(3,4) - Epsilon(1,2,3,-1)*P(-1,3)*P(4,1) - Epsilon(1,2,3,-1)*P(-1,4)*P(4,1) + Epsilon(1,2,3,-1)*P(-1,3)*P(4,2) + Epsilon(1,2,3,-1)*P(-1,4)*P(4,2) - Epsilon(1,2,3,-1)*P(-1,1)*P(4,3) + Epsilon(1,2,3,-1)*P(-1,2)*P(4,3) + (Epsilon(3,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,2))/2. - (Epsilon(3,4,-1,-2)*P(-2,4)*P(-1,1)*Metric(1,2))/2. + (Epsilon(3,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(1,2))/2. - (Epsilon(3,4,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,2))/2. - (Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,2))/2. - (Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,3)*Metric(1,2))/2. + (Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,2))/2. + (Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(1,2))/2. + (Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,3))/2. + (Epsilon(2,4,-1,-2)*P(-2,4)*P(-1,1)*Metric(1,3))/2. + (Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(1,3))/2. - (Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,3))/2. - (Epsilon(2,4,-1,-2)*P(-2,2)*P(-1,3)*Metric(1,3))/2. - (Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,3))/2. + (Epsilon(2,3,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,4))/2. + (Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,1)*Metric(1,4))/2. + (Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,4))/2. - (Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,4))/2. - (Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,4))/2. - (Epsilon(2,3,-1,-2)*P(-2,2)*P(-1,4)*Metric(1,4))/2. + (Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(2,3))/2. + (Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(2,3))/2. + (Epsilon(1,4,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,3))/2. - (Epsilon(1,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(2,3))/2. - (Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,3)*Metric(2,3))/2. - (Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,3))/2. + (Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,1)*Metric(2,4))/2. + (Epsilon(1,3,-1,-2)*P(-2,3)*P(-1,2)*Metric(2,4))/2. + (Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,4))/2. - (Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,3)*Metric(2,4))/2. - (Epsilon(1,3,-1,-2)*P(-2,1)*P(-1,4)*Metric(2,4))/2. - (Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,4))/2. - (Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*Metric(3,4))/2. - (Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,1)*Metric(3,4))/2. + (Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2)*Metric(3,4))/2. + (Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*Metric(3,4))/2. + (Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,3)*Metric(3,4))/2. - (Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,3)*Metric(3,4))/2. + (Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,4)*Metric(3,4))/2. - (Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,4)*Metric(3,4))/2.')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Epsilon(1,2,3,4)*P(-1,1)*P(-1,2) - Epsilon(1,2,3,4)*P(-1,1)*P(-1,3) - Epsilon(1,2,3,4)*P(-1,2)*P(-1,4) + Epsilon(1,2,3,4)*P(-1,3)*P(-1,4) + Epsilon(2,3,4,-1)*P(-1,1)*P(1,2) + Epsilon(2,3,4,-1)*P(-1,4)*P(1,2) - Epsilon(2,3,4,-1)*P(-1,1)*P(1,3) - Epsilon(2,3,4,-1)*P(-1,4)*P(1,3) + Epsilon(2,3,4,-1)*P(-1,2)*P(1,4) - Epsilon(2,3,4,-1)*P(-1,3)*P(1,4) - Epsilon(1,3,4,-1)*P(-1,2)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,3)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,1)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,4)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,2)*P(2,4) + Epsilon(1,3,4,-1)*P(-1,3)*P(2,4) - Epsilon(1,2,4,-1)*P(-1,2)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,3)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,1)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,4)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,2)*P(3,4) + Epsilon(1,2,4,-1)*P(-1,3)*P(3,4) + Epsilon(1,2,3,-1)*P(-1,2)*P(4,1) - Epsilon(1,2,3,-1)*P(-1,3)*P(4,1) + Epsilon(1,2,3,-1)*P(-1,1)*P(4,2) + Epsilon(1,2,3,-1)*P(-1,4)*P(4,2) - Epsilon(1,2,3,-1)*P(-1,1)*P(4,3) - Epsilon(1,2,3,-1)*P(-1,4)*P(4,3) + (Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(1,2))/2. + (Epsilon(3,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,2))/2. - (Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,2))/2. - (Epsilon(3,4,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,2))/2. - (Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,2))/2. + (Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(1,2))/2. + (Epsilon(2,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(1,3))/2. + (Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,3))/2. - (Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,3))/2. - (Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,3))/2. - (Epsilon(2,4,-1,-2)*P(-2,4)*P(-1,3)*Metric(1,3))/2. + (Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,4)*Metric(1,3))/2. - (Epsilon(2,3,-1,-2)*P(-2,2)*P(-1,1)*Metric(1,4))/2. + (Epsilon(2,3,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,4))/2. + (Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,4))/2. + (Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,4))/2. - (Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,4))/2. - (Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,3)*Metric(1,4))/2. - (Epsilon(2,3,-1,-2)*P(-2,2)*P(-1,4)*Metric(1,4))/2. + (Epsilon(2,3,-1,-2)*P(-2,3)*P(-1,4)*Metric(1,4))/2. + (Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(2,3))/2. + (Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(2,3))/2. - (Epsilon(1,4,-1,-2)*P(-2,1)*P(-1,2)*Metric(2,3))/2. + (Epsilon(1,4,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,3))/2. - (Epsilon(1,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(2,3))/2. + (Epsilon(1,4,-1,-2)*P(-2,4)*P(-1,3)*Metric(2,3))/2. - (Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,3))/2. - (Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,4)*Metric(2,3))/2. - (Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,1)*Metric(2,4))/2. + (Epsilon(1,3,-1,-2)*P(-2,1)*P(-1,2)*Metric(2,4))/2. + (Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,4))/2. + (Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,3)*Metric(2,4))/2. - (Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,4))/2. - (Epsilon(1,3,-1,-2)*P(-2,3)*P(-1,4)*Metric(2,4))/2. - (Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*Metric(3,4))/2. + (Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*Metric(3,4))/2. + (Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,3)*Metric(3,4))/2. + (Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,3)*Metric(3,4))/2. - (Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,4)*Metric(3,4))/2. - (Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,4)*Metric(3,4))/2.')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV6 = Lorentz(name = 'VVVV6',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV7 = Lorentz(name = 'VVVV7',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

VVVV8 = Lorentz(name = 'VVVV8',
                spins = [ 3, 3, 3, 3 ],
                structure = 'P(3,2)*P(4,1)*Metric(1,2) - P(3,1)*P(4,2)*Metric(1,2) + P(3,4)*P(4,2)*Metric(1,2) + P(3,1)*P(4,3)*Metric(1,2) + P(2,3)*P(4,1)*Metric(1,3) + P(2,1)*P(4,2)*Metric(1,3) - P(2,1)*P(4,3)*Metric(1,3) + P(2,4)*P(4,3)*Metric(1,3) - P(2,3)*P(3,1)*Metric(1,4) - P(2,1)*P(3,2)*Metric(1,4) - P(2,4)*P(3,2)*Metric(1,4) - P(2,3)*P(3,4)*Metric(1,4) - P(1,2)*P(4,1)*Metric(2,3) - P(1,3)*P(4,1)*Metric(2,3) - P(1,4)*P(4,2)*Metric(2,3) - P(1,4)*P(4,3)*Metric(2,3) + P(-1,1)*P(-1,2)*Metric(1,4)*Metric(2,3) + P(-1,1)*P(-1,3)*Metric(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(-1,3)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,2)*P(3,1)*Metric(2,4) + P(1,4)*P(3,2)*Metric(2,4) - P(1,2)*P(3,4)*Metric(2,4) + P(1,3)*P(3,4)*Metric(2,4) - P(-1,1)*P(-1,2)*Metric(1,3)*Metric(2,4) - P(-1,3)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,3)*P(2,1)*Metric(3,4) + P(1,4)*P(2,3)*Metric(3,4) + P(1,2)*P(2,4)*Metric(3,4) - P(1,3)*P(2,4)*Metric(3,4) - P(-1,1)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVV9 = Lorentz(name = 'VVVV9',
                spins = [ 3, 3, 3, 3 ],
                structure = 'P(3,4)*P(4,1)*Metric(1,2) + P(3,4)*P(4,2)*Metric(1,2) + P(3,1)*P(4,3)*Metric(1,2) + P(3,2)*P(4,3)*Metric(1,2) + P(2,3)*P(4,1)*Metric(1,3) - P(2,4)*P(4,1)*Metric(1,3) - P(2,3)*P(4,2)*Metric(1,3) - P(2,1)*P(4,3)*Metric(1,3) - P(2,3)*P(3,1)*Metric(1,4) + P(2,4)*P(3,1)*Metric(1,4) - P(2,4)*P(3,2)*Metric(1,4) - P(2,1)*P(3,4)*Metric(1,4) - P(1,3)*P(4,1)*Metric(2,3) + P(1,3)*P(4,2)*Metric(2,3) - P(1,4)*P(4,2)*Metric(2,3) - P(1,2)*P(4,3)*Metric(2,3) + P(-1,1)*P(-1,3)*Metric(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*Metric(1,4)*Metric(2,3) - P(1,4)*P(3,1)*Metric(2,4) - P(1,3)*P(3,2)*Metric(2,4) + P(1,4)*P(3,2)*Metric(2,4) - P(1,2)*P(3,4)*Metric(2,4) + P(-1,2)*P(-1,3)*Metric(1,3)*Metric(2,4) + P(-1,1)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,3)*P(2,1)*Metric(3,4) + P(1,4)*P(2,1)*Metric(3,4) + P(1,2)*P(2,3)*Metric(3,4) + P(1,2)*P(2,4)*Metric(3,4) - P(-1,1)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,1)*P(-1,4)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVVV1 = Lorentz(name = 'VVVVV1',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'Epsilon(2,3,4,5)*P(1,2) - Epsilon(2,3,4,5)*P(1,3) + Epsilon(1,3,4,5)*P(2,1) - Epsilon(1,3,4,5)*P(2,3) + Epsilon(1,2,4,5)*P(3,1) - Epsilon(1,2,4,5)*P(3,2) + Epsilon(3,4,5,-1)*P(-1,1)*Metric(1,2) + Epsilon(3,4,5,-1)*P(-1,2)*Metric(1,2) + Epsilon(3,4,5,-1)*P(-1,3)*Metric(1,2) + Epsilon(2,4,5,-1)*P(-1,1)*Metric(1,3) + Epsilon(2,4,5,-1)*P(-1,2)*Metric(1,3) + Epsilon(2,4,5,-1)*P(-1,3)*Metric(1,3) - (Epsilon(2,3,5,-1)*P(-1,2)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,3)*Metric(1,4))/2. + (Epsilon(2,3,4,-1)*P(-1,2)*Metric(1,5))/2. - (Epsilon(2,3,4,-1)*P(-1,3)*Metric(1,5))/2. + Epsilon(1,4,5,-1)*P(-1,1)*Metric(2,3) + Epsilon(1,4,5,-1)*P(-1,2)*Metric(2,3) + Epsilon(1,4,5,-1)*P(-1,3)*Metric(2,3) - (Epsilon(1,3,5,-1)*P(-1,1)*Metric(2,4))/2. + (Epsilon(1,3,5,-1)*P(-1,3)*Metric(2,4))/2. + (Epsilon(1,3,4,-1)*P(-1,1)*Metric(2,5))/2. - (Epsilon(1,3,4,-1)*P(-1,3)*Metric(2,5))/2. - (Epsilon(1,2,5,-1)*P(-1,1)*Metric(3,4))/2. + (Epsilon(1,2,5,-1)*P(-1,2)*Metric(3,4))/2. + (Epsilon(1,2,4,-1)*P(-1,1)*Metric(3,5))/2. - (Epsilon(1,2,4,-1)*P(-1,2)*Metric(3,5))/2.')

VVVVV2 = Lorentz(name = 'VVVVV2',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'P(5,1)*Metric(1,4)*Metric(2,3) - (P(5,2)*Metric(1,4)*Metric(2,3))/2. - (P(5,3)*Metric(1,4)*Metric(2,3))/2. - P(4,1)*Metric(1,5)*Metric(2,3) + (P(4,2)*Metric(1,5)*Metric(2,3))/2. + (P(4,3)*Metric(1,5)*Metric(2,3))/2. - (P(5,1)*Metric(1,3)*Metric(2,4))/2. + P(5,2)*Metric(1,3)*Metric(2,4) - (P(5,3)*Metric(1,3)*Metric(2,4))/2. + (P(3,1)*Metric(1,5)*Metric(2,4))/2. - (P(3,2)*Metric(1,5)*Metric(2,4))/2. + (P(4,1)*Metric(1,3)*Metric(2,5))/2. - P(4,2)*Metric(1,3)*Metric(2,5) + (P(4,3)*Metric(1,3)*Metric(2,5))/2. - (P(3,1)*Metric(1,4)*Metric(2,5))/2. + (P(3,2)*Metric(1,4)*Metric(2,5))/2. - (P(5,1)*Metric(1,2)*Metric(3,4))/2. - (P(5,2)*Metric(1,2)*Metric(3,4))/2. + P(5,3)*Metric(1,2)*Metric(3,4) + (P(2,1)*Metric(1,5)*Metric(3,4))/2. - (P(2,3)*Metric(1,5)*Metric(3,4))/2. + (P(1,2)*Metric(2,5)*Metric(3,4))/2. - (P(1,3)*Metric(2,5)*Metric(3,4))/2. + (P(4,1)*Metric(1,2)*Metric(3,5))/2. + (P(4,2)*Metric(1,2)*Metric(3,5))/2. - P(4,3)*Metric(1,2)*Metric(3,5) - (P(2,1)*Metric(1,4)*Metric(3,5))/2. + (P(2,3)*Metric(1,4)*Metric(3,5))/2. - (P(1,2)*Metric(2,4)*Metric(3,5))/2. + (P(1,3)*Metric(2,4)*Metric(3,5))/2.')

VVVVV3 = Lorentz(name = 'VVVVV3',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'Epsilon(2,3,4,5)*P(1,2) - Epsilon(2,3,4,5)*P(1,5) + Epsilon(1,3,4,5)*P(2,1) - Epsilon(1,3,4,5)*P(2,5) + Epsilon(1,2,3,4)*P(5,1) - Epsilon(1,2,3,4)*P(5,2) + Epsilon(3,4,5,-1)*P(-1,1)*Metric(1,2) + Epsilon(3,4,5,-1)*P(-1,2)*Metric(1,2) + Epsilon(3,4,5,-1)*P(-1,5)*Metric(1,2) + (Epsilon(2,4,5,-1)*P(-1,2)*Metric(1,3))/2. - (Epsilon(2,4,5,-1)*P(-1,5)*Metric(1,3))/2. - (Epsilon(2,3,5,-1)*P(-1,2)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,5)*Metric(1,4))/2. + Epsilon(2,3,4,-1)*P(-1,1)*Metric(1,5) + Epsilon(2,3,4,-1)*P(-1,2)*Metric(1,5) + Epsilon(2,3,4,-1)*P(-1,5)*Metric(1,5) + (Epsilon(1,4,5,-1)*P(-1,1)*Metric(2,3))/2. - (Epsilon(1,4,5,-1)*P(-1,5)*Metric(2,3))/2. - (Epsilon(1,3,5,-1)*P(-1,1)*Metric(2,4))/2. + (Epsilon(1,3,5,-1)*P(-1,5)*Metric(2,4))/2. + Epsilon(1,3,4,-1)*P(-1,1)*Metric(2,5) + Epsilon(1,3,4,-1)*P(-1,2)*Metric(2,5) + Epsilon(1,3,4,-1)*P(-1,5)*Metric(2,5) - (Epsilon(1,2,4,-1)*P(-1,1)*Metric(3,5))/2. + (Epsilon(1,2,4,-1)*P(-1,2)*Metric(3,5))/2. + (Epsilon(1,2,3,-1)*P(-1,1)*Metric(4,5))/2. - (Epsilon(1,2,3,-1)*P(-1,2)*Metric(4,5))/2.')

VVVVV4 = Lorentz(name = 'VVVVV4',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = '-(Epsilon(2,3,4,5)*P(1,3)) + Epsilon(2,3,4,5)*P(1,4) - Epsilon(1,3,4,5)*P(2,3) + Epsilon(1,3,4,5)*P(2,4) + Epsilon(1,2,4,5)*P(3,1) - Epsilon(1,2,4,5)*P(3,2) + Epsilon(1,2,3,5)*P(4,1) - Epsilon(1,2,3,5)*P(4,2) + Epsilon(3,4,5,-1)*P(-1,3)*Metric(1,2) - Epsilon(3,4,5,-1)*P(-1,4)*Metric(1,2) + Epsilon(2,4,5,-1)*P(-1,1)*Metric(1,3) + (Epsilon(2,4,5,-1)*P(-1,2)*Metric(1,3))/2. + Epsilon(2,4,5,-1)*P(-1,3)*Metric(1,3) + (Epsilon(2,4,5,-1)*P(-1,4)*Metric(1,3))/2. + Epsilon(2,3,5,-1)*P(-1,1)*Metric(1,4) + (Epsilon(2,3,5,-1)*P(-1,2)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,3)*Metric(1,4))/2. + Epsilon(2,3,5,-1)*P(-1,4)*Metric(1,4) - (Epsilon(2,3,4,-1)*P(-1,3)*Metric(1,5))/2. + (Epsilon(2,3,4,-1)*P(-1,4)*Metric(1,5))/2. + (Epsilon(1,4,5,-1)*P(-1,1)*Metric(2,3))/2. + Epsilon(1,4,5,-1)*P(-1,2)*Metric(2,3) + Epsilon(1,4,5,-1)*P(-1,3)*Metric(2,3) + (Epsilon(1,4,5,-1)*P(-1,4)*Metric(2,3))/2. + (Epsilon(1,3,5,-1)*P(-1,1)*Metric(2,4))/2. + Epsilon(1,3,5,-1)*P(-1,2)*Metric(2,4) + (Epsilon(1,3,5,-1)*P(-1,3)*Metric(2,4))/2. + Epsilon(1,3,5,-1)*P(-1,4)*Metric(2,4) - (Epsilon(1,3,4,-1)*P(-1,3)*Metric(2,5))/2. + (Epsilon(1,3,4,-1)*P(-1,4)*Metric(2,5))/2. - Epsilon(1,2,5,-1)*P(-1,1)*Metric(3,4) + Epsilon(1,2,5,-1)*P(-1,2)*Metric(3,4) + (Epsilon(1,2,4,-1)*P(-1,1)*Metric(3,5))/2. - (Epsilon(1,2,4,-1)*P(-1,2)*Metric(3,5))/2. + (Epsilon(1,2,3,-1)*P(-1,1)*Metric(4,5))/2. - (Epsilon(1,2,3,-1)*P(-1,2)*Metric(4,5))/2.')

VVVVV5 = Lorentz(name = 'VVVVV5',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = '-(Epsilon(1,3,4,5)*P(2,4)) + Epsilon(1,3,4,5)*P(2,5) - Epsilon(1,2,4,5)*P(3,4) + Epsilon(1,2,4,5)*P(3,5) + Epsilon(1,2,3,5)*P(4,2) - Epsilon(1,2,3,5)*P(4,3) + Epsilon(1,2,3,4)*P(5,2) - Epsilon(1,2,3,4)*P(5,3) + (Epsilon(3,4,5,-1)*P(-1,4)*Metric(1,2))/2. - (Epsilon(3,4,5,-1)*P(-1,5)*Metric(1,2))/2. + (Epsilon(2,4,5,-1)*P(-1,4)*Metric(1,3))/2. - (Epsilon(2,4,5,-1)*P(-1,5)*Metric(1,3))/2. - (Epsilon(2,3,5,-1)*P(-1,2)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,3)*Metric(1,4))/2. - (Epsilon(2,3,4,-1)*P(-1,2)*Metric(1,5))/2. + (Epsilon(2,3,4,-1)*P(-1,3)*Metric(1,5))/2. - Epsilon(1,4,5,-1)*P(-1,4)*Metric(2,3) + Epsilon(1,4,5,-1)*P(-1,5)*Metric(2,3) - Epsilon(1,3,5,-1)*P(-1,2)*Metric(2,4) - (Epsilon(1,3,5,-1)*P(-1,3)*Metric(2,4))/2. - Epsilon(1,3,5,-1)*P(-1,4)*Metric(2,4) - (Epsilon(1,3,5,-1)*P(-1,5)*Metric(2,4))/2. - Epsilon(1,3,4,-1)*P(-1,2)*Metric(2,5) - (Epsilon(1,3,4,-1)*P(-1,3)*Metric(2,5))/2. - (Epsilon(1,3,4,-1)*P(-1,4)*Metric(2,5))/2. - Epsilon(1,3,4,-1)*P(-1,5)*Metric(2,5) - (Epsilon(1,2,5,-1)*P(-1,2)*Metric(3,4))/2. - Epsilon(1,2,5,-1)*P(-1,3)*Metric(3,4) - Epsilon(1,2,5,-1)*P(-1,4)*Metric(3,4) - (Epsilon(1,2,5,-1)*P(-1,5)*Metric(3,4))/2. - (Epsilon(1,2,4,-1)*P(-1,2)*Metric(3,5))/2. - Epsilon(1,2,4,-1)*P(-1,3)*Metric(3,5) - (Epsilon(1,2,4,-1)*P(-1,4)*Metric(3,5))/2. - Epsilon(1,2,4,-1)*P(-1,5)*Metric(3,5) + Epsilon(1,2,3,-1)*P(-1,2)*Metric(4,5) - Epsilon(1,2,3,-1)*P(-1,3)*Metric(4,5)')

VVVVV6 = Lorentz(name = 'VVVVV6',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'Epsilon(2,3,4,5)*P(1,4) - Epsilon(2,3,4,5)*P(1,5) + Epsilon(1,2,3,5)*P(4,1) - Epsilon(1,2,3,5)*P(4,5) + Epsilon(1,2,3,4)*P(5,1) - Epsilon(1,2,3,4)*P(5,4) - (Epsilon(3,4,5,-1)*P(-1,4)*Metric(1,2))/2. + (Epsilon(3,4,5,-1)*P(-1,5)*Metric(1,2))/2. + (Epsilon(2,4,5,-1)*P(-1,4)*Metric(1,3))/2. - (Epsilon(2,4,5,-1)*P(-1,5)*Metric(1,3))/2. + Epsilon(2,3,5,-1)*P(-1,1)*Metric(1,4) + Epsilon(2,3,5,-1)*P(-1,4)*Metric(1,4) + Epsilon(2,3,5,-1)*P(-1,5)*Metric(1,4) + Epsilon(2,3,4,-1)*P(-1,1)*Metric(1,5) + Epsilon(2,3,4,-1)*P(-1,4)*Metric(1,5) + Epsilon(2,3,4,-1)*P(-1,5)*Metric(1,5) + (Epsilon(1,3,5,-1)*P(-1,1)*Metric(2,4))/2. - (Epsilon(1,3,5,-1)*P(-1,5)*Metric(2,4))/2. + (Epsilon(1,3,4,-1)*P(-1,1)*Metric(2,5))/2. - (Epsilon(1,3,4,-1)*P(-1,4)*Metric(2,5))/2. - (Epsilon(1,2,5,-1)*P(-1,1)*Metric(3,4))/2. + (Epsilon(1,2,5,-1)*P(-1,5)*Metric(3,4))/2. - (Epsilon(1,2,4,-1)*P(-1,1)*Metric(3,5))/2. + (Epsilon(1,2,4,-1)*P(-1,4)*Metric(3,5))/2. + Epsilon(1,2,3,-1)*P(-1,1)*Metric(4,5) + Epsilon(1,2,3,-1)*P(-1,4)*Metric(4,5) + Epsilon(1,2,3,-1)*P(-1,5)*Metric(4,5)')

VVVVV7 = Lorentz(name = 'VVVVV7',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'Epsilon(1,2,4,5)*P(3,4) - Epsilon(1,2,4,5)*P(3,5) + Epsilon(1,2,3,5)*P(4,3) - Epsilon(1,2,3,5)*P(4,5) + Epsilon(1,2,3,4)*P(5,3) - Epsilon(1,2,3,4)*P(5,4) - (Epsilon(2,4,5,-1)*P(-1,4)*Metric(1,3))/2. + (Epsilon(2,4,5,-1)*P(-1,5)*Metric(1,3))/2. - (Epsilon(2,3,5,-1)*P(-1,3)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,5)*Metric(1,4))/2. - (Epsilon(2,3,4,-1)*P(-1,3)*Metric(1,5))/2. + (Epsilon(2,3,4,-1)*P(-1,4)*Metric(1,5))/2. + (Epsilon(1,4,5,-1)*P(-1,4)*Metric(2,3))/2. - (Epsilon(1,4,5,-1)*P(-1,5)*Metric(2,3))/2. + (Epsilon(1,3,5,-1)*P(-1,3)*Metric(2,4))/2. - (Epsilon(1,3,5,-1)*P(-1,5)*Metric(2,4))/2. + (Epsilon(1,3,4,-1)*P(-1,3)*Metric(2,5))/2. - (Epsilon(1,3,4,-1)*P(-1,4)*Metric(2,5))/2. + Epsilon(1,2,5,-1)*P(-1,3)*Metric(3,4) + Epsilon(1,2,5,-1)*P(-1,4)*Metric(3,4) + Epsilon(1,2,5,-1)*P(-1,5)*Metric(3,4) + Epsilon(1,2,4,-1)*P(-1,3)*Metric(3,5) + Epsilon(1,2,4,-1)*P(-1,4)*Metric(3,5) + Epsilon(1,2,4,-1)*P(-1,5)*Metric(3,5) + Epsilon(1,2,3,-1)*P(-1,3)*Metric(4,5) + Epsilon(1,2,3,-1)*P(-1,4)*Metric(4,5) + Epsilon(1,2,3,-1)*P(-1,5)*Metric(4,5)')

VVVVV8 = Lorentz(name = 'VVVVV8',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'P(5,1)*Metric(1,3)*Metric(2,4) - P(5,4)*Metric(1,3)*Metric(2,4) - P(3,1)*Metric(1,5)*Metric(2,4) + 2*P(3,4)*Metric(1,5)*Metric(2,4) - P(3,5)*Metric(1,5)*Metric(2,4) + P(4,1)*Metric(1,3)*Metric(2,5) - P(4,5)*Metric(1,3)*Metric(2,5) - P(3,1)*Metric(1,4)*Metric(2,5) - P(3,4)*Metric(1,4)*Metric(2,5) + 2*P(3,5)*Metric(1,4)*Metric(2,5) - P(5,1)*Metric(1,2)*Metric(3,4) + P(5,4)*Metric(1,2)*Metric(3,4) + P(2,1)*Metric(1,5)*Metric(3,4) - 2*P(2,4)*Metric(1,5)*Metric(3,4) + P(2,5)*Metric(1,5)*Metric(3,4) + P(1,4)*Metric(2,5)*Metric(3,4) - P(1,5)*Metric(2,5)*Metric(3,4) - P(4,1)*Metric(1,2)*Metric(3,5) + P(4,5)*Metric(1,2)*Metric(3,5) + P(2,1)*Metric(1,4)*Metric(3,5) + P(2,4)*Metric(1,4)*Metric(3,5) - 2*P(2,5)*Metric(1,4)*Metric(3,5) - P(1,4)*Metric(2,4)*Metric(3,5) + P(1,5)*Metric(2,4)*Metric(3,5) + 2*P(3,1)*Metric(1,2)*Metric(4,5) - P(3,4)*Metric(1,2)*Metric(4,5) - P(3,5)*Metric(1,2)*Metric(4,5) - 2*P(2,1)*Metric(1,3)*Metric(4,5) + P(2,4)*Metric(1,3)*Metric(4,5) + P(2,5)*Metric(1,3)*Metric(4,5)')

VVVVV9 = Lorentz(name = 'VVVVV9',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'P(5,1)*Metric(1,4)*Metric(2,3) + P(5,2)*Metric(1,4)*Metric(2,3) - P(5,3)*Metric(1,4)*Metric(2,3) - P(5,4)*Metric(1,4)*Metric(2,3) - P(4,1)*Metric(1,5)*Metric(2,3) + P(4,3)*Metric(1,5)*Metric(2,3) + P(5,1)*Metric(1,3)*Metric(2,4) + P(5,2)*Metric(1,3)*Metric(2,4) - P(5,3)*Metric(1,3)*Metric(2,4) - P(5,4)*Metric(1,3)*Metric(2,4) - P(3,1)*Metric(1,5)*Metric(2,4) + P(3,4)*Metric(1,5)*Metric(2,4) - P(4,2)*Metric(1,3)*Metric(2,5) + P(4,3)*Metric(1,3)*Metric(2,5) - P(3,2)*Metric(1,4)*Metric(2,5) + P(3,4)*Metric(1,4)*Metric(2,5) - 2*P(5,1)*Metric(1,2)*Metric(3,4) - 2*P(5,2)*Metric(1,2)*Metric(3,4) + 2*P(5,3)*Metric(1,2)*Metric(3,4) + 2*P(5,4)*Metric(1,2)*Metric(3,4) + 2*P(2,1)*Metric(1,5)*Metric(3,4) - P(2,3)*Metric(1,5)*Metric(3,4) - P(2,4)*Metric(1,5)*Metric(3,4) + 2*P(1,2)*Metric(2,5)*Metric(3,4) - P(1,3)*Metric(2,5)*Metric(3,4) - P(1,4)*Metric(2,5)*Metric(3,4) + P(4,1)*Metric(1,2)*Metric(3,5) + P(4,2)*Metric(1,2)*Metric(3,5) - 2*P(4,3)*Metric(1,2)*Metric(3,5) - P(2,1)*Metric(1,4)*Metric(3,5) + P(2,3)*Metric(1,4)*Metric(3,5) - P(1,2)*Metric(2,4)*Metric(3,5) + P(1,3)*Metric(2,4)*Metric(3,5) + P(3,1)*Metric(1,2)*Metric(4,5) + P(3,2)*Metric(1,2)*Metric(4,5) - 2*P(3,4)*Metric(1,2)*Metric(4,5) - P(2,1)*Metric(1,3)*Metric(4,5) + P(2,4)*Metric(1,3)*Metric(4,5) - P(1,2)*Metric(2,3)*Metric(4,5) + P(1,4)*Metric(2,3)*Metric(4,5)')

VVVVV10 = Lorentz(name = 'VVVVV10',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(5,1)*Metric(1,4)*Metric(2,3) - P(5,2)*Metric(1,4)*Metric(2,3) - P(4,1)*Metric(1,5)*Metric(2,3) + 2*P(4,2)*Metric(1,5)*Metric(2,3) - P(4,5)*Metric(1,5)*Metric(2,3) - P(5,1)*Metric(1,3)*Metric(2,4) + P(5,2)*Metric(1,3)*Metric(2,4) + P(3,1)*Metric(1,5)*Metric(2,4) - 2*P(3,2)*Metric(1,5)*Metric(2,4) + P(3,5)*Metric(1,5)*Metric(2,4) + 2*P(4,1)*Metric(1,3)*Metric(2,5) - P(4,2)*Metric(1,3)*Metric(2,5) - P(4,5)*Metric(1,3)*Metric(2,5) - 2*P(3,1)*Metric(1,4)*Metric(2,5) + P(3,2)*Metric(1,4)*Metric(2,5) + P(3,5)*Metric(1,4)*Metric(2,5) - P(4,1)*Metric(1,2)*Metric(3,5) - P(4,2)*Metric(1,2)*Metric(3,5) + 2*P(4,5)*Metric(1,2)*Metric(3,5) + P(2,1)*Metric(1,4)*Metric(3,5) - P(2,5)*Metric(1,4)*Metric(3,5) + P(1,2)*Metric(2,4)*Metric(3,5) - P(1,5)*Metric(2,4)*Metric(3,5) + P(3,1)*Metric(1,2)*Metric(4,5) + P(3,2)*Metric(1,2)*Metric(4,5) - 2*P(3,5)*Metric(1,2)*Metric(4,5) - P(2,1)*Metric(1,3)*Metric(4,5) + P(2,5)*Metric(1,3)*Metric(4,5) - P(1,2)*Metric(2,3)*Metric(4,5) + P(1,5)*Metric(2,3)*Metric(4,5)')

VVVVV11 = Lorentz(name = 'VVVVV11',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(5,3)*Metric(1,4)*Metric(2,3) - P(5,4)*Metric(1,4)*Metric(2,3) + P(4,3)*Metric(1,5)*Metric(2,3) - P(4,5)*Metric(1,5)*Metric(2,3) - P(5,3)*Metric(1,3)*Metric(2,4) + P(5,4)*Metric(1,3)*Metric(2,4) + P(3,4)*Metric(1,5)*Metric(2,4) - P(3,5)*Metric(1,5)*Metric(2,4) - P(4,3)*Metric(1,3)*Metric(2,5) + P(4,5)*Metric(1,3)*Metric(2,5) - P(3,4)*Metric(1,4)*Metric(2,5) + P(3,5)*Metric(1,4)*Metric(2,5) - P(2,3)*Metric(1,5)*Metric(3,4) - P(2,4)*Metric(1,5)*Metric(3,4) + 2*P(2,5)*Metric(1,5)*Metric(3,4) + P(1,3)*Metric(2,5)*Metric(3,4) + P(1,4)*Metric(2,5)*Metric(3,4) - 2*P(1,5)*Metric(2,5)*Metric(3,4) - P(2,3)*Metric(1,4)*Metric(3,5) + 2*P(2,4)*Metric(1,4)*Metric(3,5) - P(2,5)*Metric(1,4)*Metric(3,5) + P(1,3)*Metric(2,4)*Metric(3,5) - 2*P(1,4)*Metric(2,4)*Metric(3,5) + P(1,5)*Metric(2,4)*Metric(3,5) + 2*P(2,3)*Metric(1,3)*Metric(4,5) - P(2,4)*Metric(1,3)*Metric(4,5) - P(2,5)*Metric(1,3)*Metric(4,5) - 2*P(1,3)*Metric(2,3)*Metric(4,5) + P(1,4)*Metric(2,3)*Metric(4,5) + P(1,5)*Metric(2,3)*Metric(4,5)')

VVVVV12 = Lorentz(name = 'VVVVV12',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(5,2)*Metric(1,4)*Metric(2,3) + P(5,3)*Metric(1,4)*Metric(2,3) - 2*P(5,4)*Metric(1,4)*Metric(2,3) + P(4,2)*Metric(1,5)*Metric(2,3) + P(4,3)*Metric(1,5)*Metric(2,3) - 2*P(4,5)*Metric(1,5)*Metric(2,3) - P(5,3)*Metric(1,3)*Metric(2,4) + P(5,4)*Metric(1,3)*Metric(2,4) - P(3,2)*Metric(1,5)*Metric(2,4) + P(3,5)*Metric(1,5)*Metric(2,4) - P(4,3)*Metric(1,3)*Metric(2,5) + P(4,5)*Metric(1,3)*Metric(2,5) - P(3,2)*Metric(1,4)*Metric(2,5) + P(3,4)*Metric(1,4)*Metric(2,5) - P(5,2)*Metric(1,2)*Metric(3,4) + P(5,4)*Metric(1,2)*Metric(3,4) - P(2,3)*Metric(1,5)*Metric(3,4) + P(2,5)*Metric(1,5)*Metric(3,4) + P(1,2)*Metric(2,5)*Metric(3,4) + P(1,3)*Metric(2,5)*Metric(3,4) - P(1,4)*Metric(2,5)*Metric(3,4) - P(1,5)*Metric(2,5)*Metric(3,4) - P(4,2)*Metric(1,2)*Metric(3,5) + P(4,5)*Metric(1,2)*Metric(3,5) - P(2,3)*Metric(1,4)*Metric(3,5) + P(2,4)*Metric(1,4)*Metric(3,5) + P(1,2)*Metric(2,4)*Metric(3,5) + P(1,3)*Metric(2,4)*Metric(3,5) - P(1,4)*Metric(2,4)*Metric(3,5) - P(1,5)*Metric(2,4)*Metric(3,5) + 2*P(3,2)*Metric(1,2)*Metric(4,5) - P(3,4)*Metric(1,2)*Metric(4,5) - P(3,5)*Metric(1,2)*Metric(4,5) + 2*P(2,3)*Metric(1,3)*Metric(4,5) - P(2,4)*Metric(1,3)*Metric(4,5) - P(2,5)*Metric(1,3)*Metric(4,5) - 2*P(1,2)*Metric(2,3)*Metric(4,5) - 2*P(1,3)*Metric(2,3)*Metric(4,5) + 2*P(1,4)*Metric(2,3)*Metric(4,5) + 2*P(1,5)*Metric(2,3)*Metric(4,5)')

VVVVVV1 = Lorentz(name = 'VVVVVV1',
                  spins = [ 3, 3, 3, 3, 3, 3 ],
                  structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) + Metric(1,5)*Metric(2,6)*Metric(3,4) - (Metric(1,6)*Metric(2,4)*Metric(3,5))/2. - (Metric(1,4)*Metric(2,6)*Metric(3,5))/2. - (Metric(1,5)*Metric(2,4)*Metric(3,6))/2. - (Metric(1,4)*Metric(2,5)*Metric(3,6))/2. - (Metric(1,6)*Metric(2,3)*Metric(4,5))/2. - (Metric(1,3)*Metric(2,6)*Metric(4,5))/2. + Metric(1,2)*Metric(3,6)*Metric(4,5) - (Metric(1,5)*Metric(2,3)*Metric(4,6))/2. - (Metric(1,3)*Metric(2,5)*Metric(4,6))/2. + Metric(1,2)*Metric(3,5)*Metric(4,6) + Metric(1,4)*Metric(2,3)*Metric(5,6) + Metric(1,3)*Metric(2,4)*Metric(5,6) - 2*Metric(1,2)*Metric(3,4)*Metric(5,6)')

VVVVVV2 = Lorentz(name = 'VVVVVV2',
                  spins = [ 3, 3, 3, 3, 3, 3 ],
                  structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) - (Metric(1,5)*Metric(2,6)*Metric(3,4))/2. + Metric(1,6)*Metric(2,4)*Metric(3,5) - (Metric(1,4)*Metric(2,6)*Metric(3,5))/2. - (Metric(1,5)*Metric(2,4)*Metric(3,6))/2. - (Metric(1,4)*Metric(2,5)*Metric(3,6))/2. - 2*Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,3)*Metric(2,6)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) + Metric(1,5)*Metric(2,3)*Metric(4,6) - (Metric(1,3)*Metric(2,5)*Metric(4,6))/2. - (Metric(1,2)*Metric(3,5)*Metric(4,6))/2. + Metric(1,4)*Metric(2,3)*Metric(5,6) - (Metric(1,3)*Metric(2,4)*Metric(5,6))/2. - (Metric(1,2)*Metric(3,4)*Metric(5,6))/2.')

