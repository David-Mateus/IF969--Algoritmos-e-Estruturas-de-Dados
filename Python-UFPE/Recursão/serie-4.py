# S3 = 150/20, -156/30, 162/50, -170/80,174/120, -184/170,...
def serie_3(n, num_1 =  150, num_2 = 142, den = 20, inc = 10, sin = 1):
    if n < 1:
        if n > 0:
            res = sin * num_1/den
        else:
            res = sin * num_2/den
    else:
        if n > 0:
            res = sin * num_1/den + serie_3(n-1, num_1, num_2 + 10, den + inc, inc + 10, sin * -1)
        else:
            res = sin * num_2/den + serie_3(n-1, num_1 + 12, num_2, den + inc, inc + 10, sin * -1)
    return res