# I will do an implementation of the 0/1  knapsack problem - i.e. you either take the item completely or you dont 

# the goal of the algorithm is to maximize the value within the knapsack, as it cannot bear more than its weight limit.

# the algorithm works by using recursion. It is greedy in the sense that it will simply just pick what seems best at that instance
#  and run with it

def greedy_knapsack(capacity, n): 
    

    return "n"

# this function is responsible for the heuristics, which the algorithm uses in order to decide what is the optimal solution
# at that specific time. This might however not lead to the best solution globally, therefore it is greedy
def heuristics(n):

    return "n"

def main(): 
    # defining what we are working with
    values = [100, 200, 43, 56, 34, 45] # values of items 
    weights = [23, 21, 4, 67, 34, 13] # weights of items
    capacity = 100 # maximum capacity of the knapsack
    n = len(values) # the amount of items 


    print("n")
    print(greedy_knapsack(capacity,n))


main() 
