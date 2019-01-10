import math
# from equation 4x – 5y + 33 = 0 and 20x – 9y – 107 = 0
byx = 4/5
bxy = 9/20
cc = math.sqrt(bxy*byx)#corelation coefficient
sigmax = 3
#Formula : byx = cc*(sigmay/sigmax), therefore

sigmay = (byx/cc)*sigmax
print("%.1f",%(sigmay))
