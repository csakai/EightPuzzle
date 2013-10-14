from numpuzz import NumPuzz
from NPnode import NPnode
from collections import deque
from random import shuffle as rdir

start=NumPuzz(4, [1, 'B', 2, 4, 5, 7, 3, 8, 9, 6, 11, 12, 13, 10, 14, 15], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'B'])

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
            if expanded.left!=None:
                check.append(expanded.left)
            if expanded.up!=None:
                check.append(expanded.up)
            if expanded.down!=None:
                check.append(expanded.down)
            if expanded.right!=None:
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
            if expanded.left!=None:
                check.append(expanded.left)
            if expanded.up!=None:
                check.append(expanded.up)
            if expanded.down!=None:
                check.append(expanded.down)
            if expanded.right!=None:
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
            if expanded.left!=None: fringe.append(expanded.left)
            if expanded.up!=None: fringe.append(expanded.up)
            if expanded.down!=None: fringe.append(expanded.down)
            if expanded.right!=None: fringe.append(expanded.right)
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
    while len(fringe)<10:
        fringe=sorted(fringe, reverse=True)
        expanded=fringe.pop()
        elist.append(expanded.name)
        if not expanded.isGoal():
            print(str(expanded))
            print(moardata(expanded))
            expand(expanded)
            if expanded.left!=None: fringe.append(expanded.left)
            if expanded.up!=None: fringe.append(expanded.up)
            if expanded.down!=None: fringe.append(expanded.down)
            if expanded.right!=None: fringe.append(expanded.right)
        else: print("Solution Path Found: " + expanded.name)

def moardata(node):
    s="Index of B is " + str(node.data.B)+"\n"
    s+="Weight of Path to this node is " + str(node.data.G)+"\n"
    s+="H(n)=" + str(node.data.H)+"\n"
    s+="Potential Directions is " + str(node.data.moves)+"\n"
    return s