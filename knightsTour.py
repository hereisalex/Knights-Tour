class Move():
    def __init__(self, spaceLocation, moveNumber):
        self.spaceLocation = spaceLocation
        self.moveNumber = moveNumber
        self.visitedSpaces = []
        self.parent = None
        
    def isValid(self):
        xcoord = self.spaceLocation[0]
        ycoord = self.spaceLocation[1]
        if xcoord >= 1 and xcoord <= 4 and ycoord >= 1 and ycoord <= 4 and self.spaceLocation not in self.visitedSpaces:
            return True
        else:
            return False

    def isComplete(self):
        if self.moveNumber >= 16:
            return True
        else:
            return False
        
## Tests all possible moves from the current state.
def successors(curState):
   
    children = []; ## List of valid moves from the current state
    
    ##Try moving right 2 up 1
    newState = Move([curState.spaceLocation[0] + 2, curState.spaceLocation[1] + 1], curState.moveNumber + 1)
    if newState.isValid() and newState not in children: ## Tests if new state is valid
        newState.moveNumber = curState.moveNumber + 1
        newState.visitedSpaces = curState.visitedSpaces
        newState.visitedSpaces.append(newState.spaceLocation)
        newState.parent = curState ## Sets incoming state as parent of new state
        children.append(newState) ## Adds new state to list of incoming state's children
    
    ## Try moving up 2 right 1
    newState = Move([curState.spaceLocation[0] + 1, curState.spaceLocation[1] + 2], curState.moveNumber + 1)
    if newState.isValid() and newState not in children:

        newState.moveNumber += 1
        newState.visitedSpaces = curState.visitedSpaces
        newState.visitedSpaces.append(newState.spaceLocation)
        newState.parent = curState 
        children.append(newState) 

    ## Try moving up 2 left 1
    newState = Move([curState.spaceLocation[0] - 1, curState.spaceLocation[1] + 2], curState.moveNumber + 1)
    if newState.isValid() and newState not in children:
        newState.moveNumber += 1
        print(newState.moveNumber)
        newState.visitedSpaces = curState.visitedSpaces
        newState.visitedSpaces.append(newState.spaceLocation)
        newState.parent = curState 
        children.append(newState) 

    ## Try moving left 2 up 1
    newState = Move([curState.spaceLocation[0] - 2, curState.spaceLocation[1] + 1], curState.moveNumber + 1)
    if newState.isValid() and newState not in children: 
        newState.moveNumber += 1
        newState.visitedSpaces = curState.visitedSpaces
        newState.visitedSpaces.append(newState.spaceLocation)
        newState.parent = curState 
        children.append(newState) 

    ## Try moving left 2 down 1
    newState = Move([curState.spaceLocation[0] - 2, curState.spaceLocation[1] - 1], curState.moveNumber + 1)
    if newState.isValid() and newState not in children: 
        newState.moveNumber += 1
        newState.visitedSpaces = curState.visitedSpaces
        newState.visitedSpaces.append(newState.spaceLocation)
        newState.parent = curState 
        children.append(newState) 

    ## Try moving down 2 left 1
    newState = Move([curState.spaceLocation[0] - 1, curState.spaceLocation[1] - 2], curState.moveNumber + 1)
    if newState.isValid() and newState not in children: 
        newState.moveNumber += 1
        newState.visitedSpaces = curState.visitedSpaces
        newState.visitedSpaces.append(newState.spaceLocation)
        newState.parent = curState 
        children.append(newState) 
    ## Try moving down 2 right 1


    ## Try moving right 2 down 1
    newState = Move([curState.spaceLocation[0] + 2, curState.spaceLocation[1] - 1], curState.moveNumber + 1)
    if newState.isValid() and newState not in children: 
        newState.moveNumber += 1
        newState.visitedSpaces = curState.visitedSpaces
        newState.visitedSpaces.append(newState.spaceLocation)
        newState.parent = curState 
        children.append(newState) 
    return children

def breadthFirstSearch(): ## Main search function
    initialMove = Move([1,1], 1) ## Initialize the puzzle with everything on the left
    if initialMove.isComplete(): ## Check the state against the goal
        return initialMove
    frontier = list() ## List of state objects to be explored
    explored = set() ## List of state objects already explored
    frontier.append(initialMove) ## Adds state to list to be explored
    while frontier: ## While there are states left to explore:
        state = frontier.pop(0) ## Take the first state from the 'to-be-explored' list:
        if state.isComplete(): ## Check if it's the goal state
            return state ## Returns goal state object to be used in printSolution() function
        explored.add(state) ## Add state to 'already-explored' list
        children = successors(state) ## Get list of state's children by running state through successors() function
        for child in children: ## For every state in the list of child states:
            if (child not in explored) or (child not in frontier): ## If child state unexplored and not already in frontier:
                frontier.append(child) ## Add child state to frontier list
    return None

def printSolution(solution):
    path = [] ## Creates list of state objects for solving the puzzle 
    path.append(solution) ## Adds the solution state to the list
    parent = solution.parent ## Assigns solution state's parent to variable parent
    while parent: ## For each state object that has a parent
        path.append(parent) ## Add the parent state object to the solution list
        parent = parent.parent ## And assign the parent's parent state to the variable parent

    for t in range(len(path)): ## For each state object in the path list
        state = path[len(path) - t - 1] ## Starting at the end of the list and working backwards
        print(chr(state.spaceLocation[0] + 96),",",state.spaceLocation[1])

def main():
    solution = breadthFirstSearch()
    printSolution(solution)
main()