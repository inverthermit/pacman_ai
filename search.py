# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def printCollection(collection):
    print('************collection**************')
    for element in collection.list:
        print(element)

class Node:
    def __init__(self, location, parent, action, pathCost, depth):
        self.cost = cost
        self.depth = depth
        self.location = location
        self.parent = parent
        self.action = action

def pushByCost(collection, element):
    collection.push(((element[0], element[1], element[2]), element[2]))



def searchOld(problem, collection, insertFunction=pushByCost):
    start = problem.getStartState()
    insertFunction(collection,(start,[], 0))
    # collection.push((start,[], 0))
    #((2, 1), 'South', 1)
    # printCollection(collection)
    result = []
    visited = set()
    while (not collection.isEmpty()):
        # print(stack)
        stateSpace = collection.pop()
        # print('stateSpace:',stateSpace)
        if(problem.isGoalState(stateSpace[0])):
            return stateSpace[1]
        if(stateSpace[0] in visited):
            continue
        visited.add(stateSpace[0])
        # print(visited)
        # print('In while')
        # printCollection(collection)
        #result.append(stateSpace[1])

        # print((stateSpace))
        # print(problem.getSuccessors(stateSpace[0]))
        successors = problem.getSuccessors(stateSpace[0])
        for element in successors:
            if(element[0] not in visited):
                # print(element)
                # print(stateSpace)
                # collection.push((element[0],stateSpace[1]+[element[1]],stateSpace[2]+element[2]))
                insertFunction(collection, (element[0],stateSpace[1]+[element[1]],stateSpace[2]+element[2]))

    return []

# work well for A*
def search(problem, collection, insertFunction=pushByCost):
    start = problem.getStartState()
    insertFunction(collection,(start,[], 0))
    # collection.push((start,[], 0))
    #((2, 1), 'South', 1)
    # printCollection(collection)
    result = []
    visited = set()
    while (not collection.isEmpty()):
        # print(stack)
        stateSpace = collection.pop()
        # print(stateSpace[0][0])
        # print('stateSpace:',stateSpace)
        if(problem.isGoalState(stateSpace[0][0])):
            # print('getGoal!')
            # print(stateSpace)
            return stateSpace[0][1]
        # if(stateSpace[0][0] in visited):
        #     continue
        if(stateSpace[0][0] in visited):
            continue
        visited.add(stateSpace[0][0])
        # print(visited)
        # print('In while')
        # printCollection(collection)
        #result.append(stateSpace[1])

        # print((stateSpace))
        # print(problem.getSuccessors(stateSpace[0]))
        successors = problem.getSuccessors(stateSpace[0][0])
        for element in successors:
            insertFunction(collection, (element[0],stateSpace[0][1]+[element[1]],stateSpace[0][2]+element[2]))

    return []
def search2(problem, collection, insertFunction=pushByCost):
    start = problem.getStartState()
    insertFunction(collection,(start,[], 0))
    # collection.push((start,[], 0))
    #((2, 1), 'South', 1)
    # printCollection(collection)
    result = []
    # visited = set()
    while (not collection.isEmpty()):
        # print(stack)
        stateSpace = collection.pop()
        print('stateSpace:',stateSpace)
        if(problem.isGoalState(stateSpace[0])):
            return stateSpace[1]
        # if(stateSpace[0] in visited):
        #     continue
        # visited.add(stateSpace[0])
        # print(visited)
        # print('In while')
        # printCollection(collection)
        #result.append(stateSpace[1])

        # print((stateSpace))
        # print(problem.getSuccessors(stateSpace[0]))
        successors = problem.getSuccessors(stateSpace[0])
        for element in successors:
            insertFunction(collection, (element[0],stateSpace[1]+[element[1]],stateSpace[2]+element[2]))

    return []

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    collection = util.Stack()
    result = search(problem, collection)
    return result

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    collection = util.Queue()
    result = search(problem, collection)
    print(result)
    return result

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    def priorityFunction(stateSpace):
        return stateSpace[1]
    collection = util.PriorityQueueWithFunction(priorityFunction)
    result = search(problem, collection)
    return result



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    def pushByCostHeuristic(collection, element, heuristic = heuristic, problem = problem):
        fn = element[2] + heuristic(element[0], problem)
        collection.push(((element[0], element[1], element[2]), fn))
    def priorityFunction(stateSpace):
        return stateSpace[1]
    collection = util.PriorityQueueWithFunction(priorityFunction)
    result = search(problem, collection, pushByCostHeuristic)
    return result


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
