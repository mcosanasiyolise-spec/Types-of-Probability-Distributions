# Suppose that we expect it to rain 10 times in the next 30 days. The number of times it rains in the next 30 days is "Poisson distributed" with lambda = 10. Calculate the probability of exactly 6 days of rain. Also, calculate the probability of 12-14 days of rain.
# Poisson Distribution = how many x events happen in fixed trials
import scipy.stats as stats

# expected value = 10, probability of observing 6
prob1 = stats.poisson.pmf(6, 10)
print("probability of raining for the eaxactly 6 days ;", prob1)

# expected value = 10, probability of observing 12-14
prob2 = stats.poisson.pmf(12, 10) + stats.poisson.pmf(14, 10)
print("probability of raining for 12-14 days :", prob2)