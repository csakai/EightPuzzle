from numpuzz import NumPuzz
from NPnode import NPnode
from collections import deque
from random import shuffle as rdir

start=NumPuzz(4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'B'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'B'])

def Randomize(complexity, start):
    dirs=list()
    for n in range(complexity):
        for (k,v) in start.moves.items():
            if v: dirs.append(k)
        rdir(dirs)
        to=dirs.pop()

        if to is "R":
            start=start.right()
            to="L"
        elif to is "U":
            start=start.up()
            to="D"
        elif to is "D":
            start=start.down()
            to="U"
        elif to is "L":
            start=start.left()
            to="R"
        if n==complexity-1:
            start.moves[to]=True
        dirs.clear()
    start.F=0
    print("Puzzle can be solved in at least " + str(complexity) + " moves.")
    return start

def DFS(start):
    fringe=[NPnode(start, "Start")]
    expanded=fringe[0]
    if expanded.isGoal():
        return "Puzzle is already solved."
    elist=list()
    check=list()
    while len(fringe)>0:
        expanded=fringe.pop()
        elist.append(expanded.name)
        if not expanded.isGoal():
            print(str(expanded))
            expand(expanded)
            if expanded.left:
                check.append(expanded.left)
            if expanded.up:
                check.append(expanded.up)
            if expanded.down:
                check.append(expanded.down)
            if expanded.right:
                check.append(expanded.right)
            for n in fringe:
                for m in check:
                    if n.isIdentical(m): check.remove(m)
                if not check: break
            else:
                fringe.extend(check)
        else: return "Solution Path Found: " + expanded.name
    return "No Solution"

def BFS(start):
    fringe=deque([NPnode(start, "Start")])
    expanded=fringe[0]
    if expanded.isGoal():
        return "Puzzle is already solved."
    elist=list()
    check=list()
    while len(fringe)>0:
        expanded=fringe.popleft()
        elist.append(expanded.name)
        if not expanded.isGoal():
            print(str(expanded))
            expand(expanded)
            if expanded.left:
                check.append(expanded.left)
            if expanded.up:
                check.append(expanded.up)
            if expanded.down:
                check.append(expanded.down)
            if expanded.right:
                check.append(expanded.right)
            for n in fringe:
                for m in check:
                    if n.isIdentical(m): check.remove(m)
                if not check: break
            else:
                fringe.extend(check)
        else: return "Solution Path Found: " + expanded.name
    return "No Solution"

def Astar(start):
    fringe=[NPnode(start, "Start")]
    expanded=fringe[0]
    if expanded.isGoal():
        return "Puzzle is already solved."
    elist=list()
    while len(fringe)>0:
        fringe=sorted(fringe, reverse=True)
        expanded=fringe.pop()
        elist.append(expanded.name)
        if not expanded.isGoal():
            print(str(expanded))
            expand(expanded)
            if expanded.left: fringe.append(expanded.left)
            if expanded.up: fringe.append(expanded.up)
            if expanded.down: fringe.append(expanded.down)
            if expanded.right: fringe.append(expanded.right)
        else: return "Solution Path Found: " + expanded.name
    return "No Solution"

def expand(node):
    node.next()

def AstarDiagnostic(start):
    fringe=[NPnode(start, "Start")]
    expanded=fringe[0]
    if expanded.isGoal():
        print("Puzzle is already solved.")
    elist=list()
    while len(fringe)<600:
        fringe=deque(sorted(fringe, key=lambda state: state.data.H, reverse=True))
        expanded=fringe.pop()
        elist.append(expanded.name)
        if not expanded.isGoal():
            print(str(expanded))
            print(moardata(expanded))
            expand(expanded)
            if expanded.left: fringe.append(expanded.left)
            if expanded.up: fringe.append(expanded.up)
            if expanded.down: fringe.append(expanded.down)
            if expanded.right: fringe.append(expanded.right)
        else: print("Solution Path Found: " + expanded.name)

def moardata(node):
    s="Index of B is " + str(node.data.B)+"\n"
    s+="Weight of Path to this node is " + str(node.data.F)+"\n"
    s+="Estimated Weight to Goal is " + str(node.data.G)+"\n"
    s+="H(n)=" + str(node.data.H)+"\n"
    s+="Potential Directions is " + str(node.data.moves)+"\n"
    return s

#the following function is a culmination for the search functions.
#To use it, just input
def search(fun, start, depth=None, it=False, debug=False):
    '''This function allows you to run all tree-based search functions. All you need to do is 
        provide the type of next-node selection to the parameter 'fun'. If you are using Depth-Limited
        Search, then you provide depth, otherwise that parameter is unnecessary. This function will
        return a tuple holding a string with the solution path and information, and a list of all
        expanded nodes' names if you wish to analyze them.'''
    if start.isGoal():
        return ("Puzzle is already solved.", list())
    else:
        if it: depth=1
        fringe=deque([NPnode(start, "Start")])
        elist=list()
        while len(fringe)>0:
            expanded, fringe = fun(fringe)
            elist.append(expanded.name)
            if fun==astarselect: elist[len(elist)-1]+=" H=" +str(expanded.data.H)
            if not expanded.isGoal():
                if debug and (not it or (it and expanded.F==depth)):
                    print(str(expanded)) #<--for debugging...
                if not depth or (depth-1)>=expanded.F:
                    expand(expanded)
                    check=list()
                    if expanded.left:
                        check.append(expanded.left)
                    if expanded.up:
                        check.append(expanded.up)
                    if expanded.down:
                        check.append(expanded.down)
                    if expanded.right:
                        check.append(expanded.right)
                    for n in range(len(fringe)):
                        for m in check:
                            if fringe[n].isIdentical(m):
                                if fringe[n].F<m.F:
                                    fringe[n]=m
                                check.remove(m)
                        if not check: break
                    else:
                        fringe.extend(check)
                elif it and not fringe:
                    depth+=1
                    fringe.append(NPnode(start, "Start"))
            else:
                return (stringifyResults(expanded, fun, depth, it), elist)
        if depth:
            return ("No solution found within " +str(depth)+" moves.", elist)
        else:
            return ("No solution found using "+searchName(fun), elist)
def astarselect(fringe):
    fringe=deque(sorted(fringe, key=lambda state: state.data.H, reverse=True))
    expanded=fringe.pop()
    return (expanded, fringe)

def uniformselect(fringe):
    fringe=deque(sorted(fringe, key=lambda state: state.F, reverse=True))
    expanded=fringe.pop()
    return (expanded, fringe)

def depthselect(fringe):
    expanded=fringe.pop()
    return (expanded, fringe)

def breadthselect(fringe):
    expanded=fringe.popleft()
    return (expanded, fringe)

def stringifyResults(Solution, fun, depth=None, it=False):
    '''returns a String with the Solution Path, search type, cost, and max depth allowed (if applicable)'''
    res=str(Solution.data.size-1)+"-Puzzle using "
    res+=searchName(fun, depth, it)
    res+="\nSolution Path Found in "
    res+=str(Solution.F)
    res+=" moves:\n"+Solution.name
    return res

def searchName(fun, depth=None, it=False):
    if fun==astarselect:
        return "A* Search"
    elif fun==uniformselect:
        return "Uniform Cost Search"
    elif fun==depthselect:
        if not depth: return "Depth-First Search"
        elif it: return "Iterative-Deepening"
        else: return "Depth-Limited Search with limit at " +str(depth)
    elif fun==breadthselect:
        return "Breadth-First Search"