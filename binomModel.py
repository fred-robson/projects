#Calculates the value of a European call option using the binomial model


#Returns the value of a hedge ratio
def hedgeRatio(d_low, d_high,s_low,s_high):
    return (d_high-d_low)/(s_high-s_low)

#Returns the value of a loan
def loanValue(hedge, s_low, d_low):
    return hedge*s_low - d_low

#Returns the value of a call option
#s0: Current stock price
#percent_up: The percentage increase that can occur for the stock each time period
#percent_down: The percentage decrease that can occur for the stock each time period
#exercise_price: The exercise price of the call
#curr_t: The current time period
#final_t: The number of time periods that the option lasts for
#r: the risk free interest rate
def valueOfCall(s0, percent_up, percent_down,exercise_price,  curr_t, final_t, r):
    s_plus = s0*(1+percent_up)
    s_minus= s0*(1-percent_down)
    d_plus = 0
    d_minus = 0
    #base case - at the end of the tree
    if(curr_t == final_t):
       d_plus = max(s_plus - exercise_price, 0)
       d_minus = max(s_minus - exercise_price, 0)
    else:
        #recursively works out the value of d_plus and d_minus
        curr_t = curr_t+1
        d_plus = valueOfCall(s_plus,percent_up, percent_down, exercise_price, curr_t, final_t, r)
        d_minus = valueOfCall(s_minus, percent_up, percent_down, exercise_price, curr_t, final_t, r) 
        #
    hedge = hedgeRatio(d_minus,d_plus, s_minus, s_plus)
    loan = loanValue(hedge,s_minus,d_minus)
    call_value = hedge*s0 - loan/(1+r)
    # print(str(call_value) + '\n')
    return call_value

#change values for different results 
curr_t = 0
s0 = 100
percent_up = 0.05
percent_down = 0.02
r = 0.005
#A two period option will have t = 1
final_t = 2
exercise_price = 104

print(valueOfCall(s0,percent_up,percent_down,exercise_price,curr_t,final_t,r))
