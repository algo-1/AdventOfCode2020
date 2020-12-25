DIVISOR = 20201227

def trans(num, loop_size, DIVISOR):
    i = 0
    val = 1
    while i < loop_size:
        val *= num
        val = val % DIVISOR
        i += 1

    return val 

# card 
dp = {}
value = 0
i = 0 
while value != 14082811:
    if i == 0:
        temp = 7
    else:
        temp = dp[i-1] * 7
    value = temp % DIVISOR
    dp[i] = value 
    i += 1


# to calc encryption key
# num = door public key 5249543
# loop_size = card_loop_size 

print(f"ans = {trans(5249543, i, DIVISOR)}")

14082811 # -> card
5249543  # -> door 

# BRUTE FORCE DIE haha

# v  = 0 
# i = 1
# while v !=  17807724: -> example input 
#     v = trans(7, i, DIVISOR)
#     i += 1
# print(i-1)

