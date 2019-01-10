phy_score = [15,12,8,8,7,7,7,6,5,3] 
hist_score = [10,25,17,11,13,17,20,13,9,15]
n = len(phy_score)
phy_hist = sum([i*j for (i,j) in zip(phy_score,hist_score)])
sum_phy = sum(phy_score)
sum_hist = sum(hist_score)
phy_sq = sum([i**2 for i in phy_score])

slope = (n*phy_hist - sum_phy*sum_hist) / (n*phy_sq - sum_phy*sum_phy)
constant = (sum_hist*phy_sq - sum_phy*phy_hist) / (n*phy_sq - sum_phy*sum_phy)
print(10*slope + constant)
