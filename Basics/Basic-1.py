# Tom and Jerry

# Tom and Jerry play a game with a number N. They will play the game alternatively and each of them would subtract a number n [n such that N%n = 0. 
# The game is repeated turn by turn until the one, who now cannot make a further move loses the game. 
# The game begins with Tom playing the first move. It is well understood that both of them will make moves in an optimal way. The task is to determine who wins the game.

# Constant time and space

def numsGame(N):
        
    # So basically if the remainder finally is 1; Tom Wins
    # If its zero, jerry wins
        
    if N%2==0:
        return 1
    return 0
  
  
# Check Balanced Number
# Given off digit number, check if sum(left) digits == sum(right) digit wrt centre
  
# Method 1:
# Time = O(len(n)/2)
# Space - constant

def balancedNumber(N):
	
    mid = len(str(N))//2

    left = 0
    right = 0

    for i in range(mid):
        left += int(str(N)[i])
        right += int(str(N)[mid+1+i])

    if left == right:
        return 1
    return 0
	
print(balancedNumber(12321))

