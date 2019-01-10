import math
phy_score = [15,12,8,8,7,7,7,6,5,3]
hist_score = [10,25,17,11,13,17,20,13,9,15]
n = len(phy_score)
phy_mean = sum(phy_score)/n
hist_mean = sum(hist_score)/n
phy_diff = [x - phy_mean for x in phy_score]
hist_diff = [x - hist_mean for x in hist_score]
phy_sd = math.sqrt((1/(n-1))*sum([x*x for x in phy_diff]))
hist_sd = math.sqrt((1/(n-1))*sum([x*x for x in hist_diff]))
print((sum([phy_score[i]*hist_score[i] for i in range(int(n))]) - n * phy_mean * hist_mean) / ((n-1) * phy_sd * hist_sd))
