# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    startingPoint = problem.getStartState() #Grabbing the starting point of the maze
    statesStack = util.Stack() #Creating a stack for the states to be place in
    
    if problem.isGoalState(startingPoint) == True: #If the starting point is the goal, return
        return []

    visitedStates = set() #Creating a set of visited states
    visitedStates.add(startingPoint) #adding initial starting point
    state = (startingPoint, []) #Creating a state with the starting point info
    statesStack.push(state) #Putting the starting state onto the stack
    
    while (statesStack.isEmpty()) == False: #Loop until the statestack is empty
        currentState = statesStack.pop() #Grab the top state off the stack
        visitedStates.add(currentState[0]) #Add new coordinates to the visited set
        trail = currentState[1] #Grabbing the trail in which has the actions to get to current state
        if problem.isGoalState(currentState[0]) == True:
            return trail
        successors = problem.getSuccessors(currentState[0]) #Grab all possibly options from current position
        
        for i in range(0, len(successors)): #For each state in the sucessors
            tempTrail = list(trail) #Creating a temp trail with previous trail in it
            position = successors[i][0] #Grab the coordinate of successor
            action = successors[i][1] #The action to get to successor
            
            if not position in visitedStates: #As long as the coordinates have not been visited yet, continue
                #Add the proper action to the action trail
                tempTrail.append(action)
                statesStack.push((position, tempTrail)) #Add the new trail to the state stack
    return []



def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """

    startingPoint = problem.getStartState() #Grabbing the starting point of the maze
    statesStack = util.Queue() #Creating a stack for the states to be place in
    
    if problem.isGoalState(startingPoint) == True: #If the starting point is the goal, return
        return []
    
    visitedStates = list() #Creating a set of visited states
    visitedStates.append(startingPoint) #Adding initial starting point to stack
    state = (startingPoint, []) #Creating a state with the starting point info
    statesStack.push(state) #Putting the starting state onto the stack
    
    while (statesStack.isEmpty()) == False: #Loop until the statestack is empty
        currentState = statesStack.pop() #Grab the top state off the stack
        trail = currentState[1] #Grabbing the trail in which has the actions to get to current state
        if problem.isGoalState(currentState[0]) == True:
            return trail
        successors = problem.getSuccessors(currentState[0]) #Grab all possibly options from current position
        
        for i in range(0, len(successors)): #For each state in the sucessors
            tempTrail = list(trail) #Creating a temp trail with previous trail in it
            position = successors[i][0] #Grab the coordinate of successor
            action = successors[i][1] #The action to get to successor
            
            if not position in visitedStates: #As long as the coordinates have not been visited yet, continue
                #Add the proper action to the action trail
                tempTrail.append(action)
                visitedStates.append(position) #Add new coordinates to the visited set
                statesStack.push((position, tempTrail)) #Add the new trail to the state stack
    return []



def uniformCostSearch(problem):

    startingPoint = problem.getStartState() #Grabbing the starting point of the maze
    statesStack = util.PriorityQueue() #Creating a stack for the states to be place in
    
    if problem.isGoalState(startingPoint) == True: #If the starting point is the goal, return
        return []
    
    visitedStates = set([]) #Creating a set of visited states
    state = (startingPoint, [], 0.0) #Creating a state with the starting point info
    statesStack.push(state, 0) #Putting the starting state onto the stack
    
    while (statesStack.isEmpty()) == False: #Loop until the statestack is empty
        currentState = statesStack.pop() #Grab the top state off the stack
        trail = currentState[1] #Grabbing the trail in which has the actions to get to current state
        if problem.isGoalState(currentState[0]) == True: #Check if we are at goal
            return trail
        if not currentState[0] in visitedStates: #THIS IS USED BECAUSE WE DONT WANT TO EXPAND NODES MULTIPLE TIMES
            visitedStates.add(currentState[0]) #Add new coordinates to the visited set
            successors = problem.getSuccessors(currentState[0]) #Grab all possibly options from current position
            for i in range(0, len(successors)): #For each state in the sucessors
                tempTrail = list(trail) #Creating a temp trail with previous trail in it
                position = successors[i][0] #Grab the coordinate of successor
                action = successors[i][1] #The action to get to successor
                cost = successors[i][2] + currentState[2] #grab total cost of action
                
            
                if not position in visitedStates: #As long as the coordinates have not been visited yet, continue
                    tempTrail.append(action) #add action to trail
                    statesStack.push((position, tempTrail, cost), cost) #Add the new trail to the state stack but prioritize by total cost
    return []

def greedySearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """

    startingPoint = problem.getStartState() #Grabbing the starting point of the maze
    statesStack = util.Queue() #Creating a stack for the states to be place in
    
    if problem.isGoalState(startingPoint) == True: #If the starting point is the goal, return
        return []
    
    visitedStates = list([startingPoint]) #Creating a set of visited states
    state = (startingPoint, []) #Creating a state with the starting point info
    statesStack.push(state) #Putting the starting state onto the stack
    
    while (statesStack.isEmpty()) == False: #Loop until the statestack is empty
        currentState = statesStack.pop() #Grab the top state off the stack
        currentPos = currentState[0] #Grabbing the coordinates of the state
        trail = currentState[1] #Grabbing the trail in which has the actions to get to current state
        if problem.isGoalState(currentState[0]) == True:
            return trail
        successors = problem.getSuccessors(currentState[0]) #Grab all possibly options from current position
        
        for i in range(0, len(successors)): #For each state in the sucessors
            tempTrail = list(trail) #Creating a temp trail with previous trail in it
            position = successors[i][0] #Grab the coordinate of successor
            action = successors[i][1] #The action to get to successor
            
            if not position in visitedStates: #As long as the coordinates have not been visited yet, continue
                #Add the proper action to the action trail
                tempTrail.append(action)
                visitedStates.append(position) #Add new coordinates to the visited set
                statesStack.push((position, tempTrail)) #Add the new trail to the state stack
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """

    startingPoint = problem.getStartState() #Grabbing the starting point of the maze
    statesStack = util.PriorityQueue() #Creating a stack for the states to be place in
    
    if problem.isGoalState(startingPoint) == True: #If the starting point is the goal, return
        return []
    
    visitedStates = list() #Creating a set of visited states
    state = (startingPoint, [], 0.0, 0.0) #Creating a state with the starting point info
    statesStack.push(state, 0) #Putting the starting state onto the stack
    
    while (statesStack.isEmpty()) == False: #Loop until the statestack is empty
        i = 0
        currentState = statesStack.pop() #Grab the top state off the stack
        currentPos = currentState[0] #Grabbing the coordinates of the state
        trail = currentState[1] #Grabbing the trail in which has the actions to get to current state
        if problem.isGoalState(currentState[0]) == True:
            return trail
        if not currentState[0] in visitedStates:#THIS IS USED BECAUSE WE DONT WANT TO EXPAND NODES MULTIPLE TIMES
            visitedStates.append(currentState[0]) #Add new coordinates to the visited set
            successors = problem.getSuccessors(currentState[0]) #Grab all possibly options from current position
            while(i < len(successors)):
                #For each successor below, I take the total cost from parent node, subtract the heuristic from it
                #and then add the successors heuristic to it.
                successors[i] = (successors[i][0], successors[i][1], successors[i][2], (currentState[3] - heuristic(currentState[0], problem)) + successors[i][2] + heuristic(successors[i][0], problem))
                i = i + 1
            for i in range(0, len(successors)): #For each state in the sucessors
                tempTrail = list(trail) #Creating a temp trail with previous trail in it
                position = successors[i][0] #Grab the coordinate of successor
                action = successors[i][1] #The action to get to successor
                cost = successors[i][2] #Cost to take action
                heuristicCost = successors[i][3] #Heuristic cose if action taken
            
                if not position in visitedStates: #As long as the coordinates have not been visited yet, continue
                    tempTrail.append(action) #Add proper action to the trail
                    statesStack.push((position, tempTrail, cost, heuristicCost), heuristicCost) #Add the new trail to the state stack but prioritized by heuristic total cost
    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
